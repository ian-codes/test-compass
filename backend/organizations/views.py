from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import HttpResponse
import json

from .models import Organization, UserProfile, Roles, OrganizationInvite
from rest_framework.authtoken.models import Token 
from .schemas import APP_SIGNUP_BODY_SCHEMA
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.core.exceptions import PermissionDenied, ValidationError
from django.utils import timezone
import hashlib
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
import jsonschema
from django.contrib.auth.password_validation import validate_password
from jsonschema import ValidationError as SchemaValidationError
from datetime import datetime
class SignupView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Validate json through schema  
        try:
            form_data = json.loads(request.body)
            jsonschema.validate(
                form_data,
                schema=APP_SIGNUP_BODY_SCHEMA,
                format_checker=jsonschema.Draft202012Validator.FORMAT_CHECKER,
            )
        except SchemaValidationError as err:
            return HttpResponse(err, status=400)

        email = form_data.get("email")


        user = None
        token = None

        try:
            user = User.objects.get(email__iexact=email)
            if User:
                msg = "A user with this email is already registered"
                return HttpResponse(msg, status=400)
        except User.DoesNotExist:
            pass

        try:
            validate_password(form_data.get("password"))
        except ValidationError as verr:
            return HttpResponse(verr, status=400)        

        username = str(form_data.get("email")).split("@")[0]

        new_user = User.objects.create(
                first_name=form_data.get("first_name"),
                last_name=form_data.get("last_name"),
                email=form_data.get("email"),
                username=username,

        )
        new_user.set_password(form_data.get("password"))
        new_user.save()
        token = Token.objects.get(user=new_user)

        if(form_data.get("organization_name")):
            organization = Organization.objects.create(name=form_data.get("organization_name"))
            profile = UserProfile.objects.get(user=new_user)
            profile.organization = organization
            profile.role = Roles.ORGANIZATION_LEADER
            profile.save()

        
        return JsonResponse({"token": token.key}, status=201)


class UserInviteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form_data = json.loads(request.body)
        token = Token.objects.get(key=request.headers.get("Authorization"))
        try:
            requesting_user = token.user
        except User.DoesNotExist:
            return HttpResponse("You have no permission ", status=403)
        
        invited_user = None
        try:
            invited_user = User.objects.get(email=form_data.get("email"))

        except User.DoesNotExist:
            return HttpResponse("User with this E-Mail doesn't exist", status=400)
        print(requesting_user.email)
        hash_data = f"{requesting_user.pk}/{timezone.now()}"
        hash_object = hashlib.sha256()
        hash_object.update(hash_data.encode('utf-8'))

        generated_hash = hash_object.hexdigest()
        expired_on = None
        if(form_data.get("expired_on")):
            expired_on = datetime.strptime(form_data.get("expired_on"), '%Y-%m-%d %H:%M:%S')
        invite_organization = UserProfile.objects.get(user=requesting_user).organization
        invite = OrganizationInvite.objects.create(
            user=invited_user, 
            organization=invite_organization,
            hash=generated_hash,
            expired_on = expired_on
            )
        
        subject = f"Einladung zu Organisation {invite_organization.name}"
        c = {
                            'invite_link': f"http://localhost:8000/organization/{invite_organization.pk}/invite/{generated_hash}",
                            'organization': invite_organization,
                            "user": invited_user,
            }
        email = render_to_string("organizations/email_templates/invite_notification.txt", c)
        try:
            send_mail(subject, email, 'noreply.testcompass@gmail.com' , [invited_user.email], fail_silently=False)

        except BadHeaderError:
                print("failed")

        return HttpResponse("Invitation sent", status=200)
    
class OrgInvitationView(View):
    def get(self, request, hash, pk, *args, **kwargs):
        organization = Organization.objects.get(pk=pk)
        invite= None
        try:
            invite = OrganizationInvite.objects.get(hash=hash, organization=organization)

            if invite.is_active == False or (invite.expired_on is not None and invite.expired_on <= timezone.now()):
                msg = "Invitation is no longer active"
                return HttpResponse(msg, status=400)
            

            profile = UserProfile.objects.get(user=invite.user)
            profile.organization = organization
            profile.role = Roles.EMPLOYEE

            invite.is_active = False
            profile.save()
            invite.save()


        except OrganizationInvite.DoesNotExist:
            msg = "Invitation does not exist"
            return HttpResponse(msg, status=400)
        
            
        return HttpResponseRedirect("https://google.com/")