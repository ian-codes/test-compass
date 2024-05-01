from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import HttpResponse
import json
from .models import Organization, UserProfile, Roles
from rest_framework.authtoken.models import Token 
from .schemas import APP_SIGNUP_BODY_SCHEMA
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, Http404
from django.core.exceptions import PermissionDenied, ValidationError

import jsonschema
from django.contrib.auth.password_validation import validate_password
from jsonschema import ValidationError as SchemaValidationError

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
            profile = UserProfile.objects.create(organization=organization, role=Roles.ORGANIZATION_LEADER, user=new_user)

        
        return JsonResponse({"token": token.key}, status=201)


            


