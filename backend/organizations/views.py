from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import HttpResponse
import json
from rest_framework.views import APIView
from django.core.mail import EmailMultiAlternatives
from .models import Organization, UserProfile, Roles, OrganizationInvite, Token

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
import datetime
from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware import csrf
from django.contrib.auth import authenticate
from testcompass_backend import settings
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class ObjectView(APIView):

    def get(self, request):
        print(request.get)
    
class RestrictedView(APIView):
    def get(self, request):
        return Response(data={"message": "This is a restricted area, welcome!"})

class LogoutView(APIView):
    permission_classes = ()

    def post(self, request):
        try:
            token = Token.objects.get(key=request.COOKIES.get('auth_token'))
        except:
            return Response({"error": "Token not found"}, status=400)

        if token:
            token.delete()
            response = Response({"message": "Logout successful"}, status=200)
            response.delete_cookie('auth_token')
            response.delete_cookie('csrf_token')
            return response

        return Response({"error": "Token not found"}, status=400)
        
class LoginView(APIView):
    permission_classes = ()  # Allows unauthenticated access

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        response = Response()  
        user = authenticate(request, username=username, password=password)
        if user is not None:

            token=None
            try:
                token = Token.objects.get(user=user)
                
                token.delete()
            except Token.DoesNotExist:

                pass
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            token = Token.objects.create(user=user, key=str(access_token))
            # response.set_cookie('auth_token', str(access_token), httponly=True, expires=datetime.timedelta(days=30))

            response.set_cookie(
                key='auth_token',
                value=str(access_token),
                httponly=True,
                expires=datetime.timedelta(days=30),
                secure=True,
                samesite='None'
            )

            csrf.get_token(request)
            response.data = {
                'login successful'
            }
            return response
        return Response({'error': 'Invalid Credentials'}, status=401)
    
class SignupView(APIView):
    permission_classes = () 
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
                username=form_data.get("email"),

        )
        new_user.set_password(form_data.get("password"))
        new_user.save()

        refresh = RefreshToken.for_user(new_user)
        access_token = refresh.access_token
        response = Response() 
        token = Token.objects.create(user=new_user, key=str(access_token))
        response.set_cookie('auth_token', str(access_token), httponly=True, expires=datetime.timedelta(days=30))
        csrf.get_token(request)
        if(form_data.get("organization_name")):
            organization = Organization.objects.create(name=form_data.get("organization_name"))
            profile = UserProfile.objects.get(user=new_user)
            profile.organization = organization
            profile.role = Roles.ORGANIZATION_LEADER
            profile.save()

        response.data = {
                'signup successful'
        }
        
        return response


class UserInviteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form_data = json.loads(request.body)
        token = Token.objects.get(key=request.COOKIES.get('auth_token'))
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