import json
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, ListView, TemplateView, CreateView, DetailView
from django.http import JsonResponse, HttpResponse, Http404
from .models import UserAcceptanceTest, UserAcceptanceTestResult, TestProcedureResult, TestProcedure, User, Project
from organizations.models import UserProfile, Organization

class TestView(View):
    def get(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.COOKIES.get('auth_token'))
        user=token.user
        profile = UserProfile.objects.get(user=user)
        if not profile.organization:
            return HttpResponse(
                "This user has no organization", status=400
            )
        project = None
        try:    
            project = Project.objects.get(pk=kwargs.get('pk'))        

        except Project.DoesNotExist:
          return HttpResponse(
                "Project with pk does not exist", status=400
            )        
        
        if not user in project.user_list.all():
            return HttpResponse(
                "Unauthorized", status=403
            )        

        tests = UserAcceptanceTest.objects.filter(project=project)
        test_list = list(tests.values())

        return JsonResponse(test_list, safe=False)


class TestResultView(View):
    def get(self, request, *args, **kwargs):

        token = Token.objects.get(key=request.COOKIES.get('auth_token'))
        user=token.user
        profile = UserProfile.objects.get(user=user)
        if not profile.organization:
            return HttpResponse(
                "This user has no organization", status=400
            )
        project = None
        try:    
            project = Project.objects.get(pk=kwargs.get('pk'))        

        except Project.DoesNotExist:
          return HttpResponse(
                "Project with pk does not exist", status=400
            )        
        
        if not user in project.user_list.all():
            return HttpResponse(
                "Unauthorized", status=403
            )
        acceptance_test = UserAcceptanceTest.objects.get(pk=kwargs.get('pk'))      
        test_results = UserAcceptanceTestResult.objects.filter(test)
        test_result_list = list(test_results.values())

        return JsonResponse(test_result_list, safe=False)


class TestProcedureView(View):
    def get(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.COOKIES.get('auth_token'))
        user=token.user
        profile = UserProfile.objects.get(user=user)
        if not profile.organization:
            return HttpResponse(
                "This user has no organization", status=400
            )
        project = None
        try:    
            project = Project.objects.get(pk=kwargs.get('pk'))        

        except Project.DoesNotExist:
          return HttpResponse(
                "Project with pk does not exist", status=400
            )        
        
        if not user in project.user_list.all():
            return HttpResponse(
                "Unauthorized", status=403
            )
        test_procedures = TestProcedure.objects.filter(project=project)

        test_procedure_list = list(test_procedures.values())

        return JsonResponse(test_procedure_list, safe=False)


class TestProcedureResultView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            test_procedure_results = TestProcedureResult.objects.filter(creator=self.request.user)
        else:
            test_procedure_results = None

        test_procedure_result_list = list(test_procedure_results.values())

        return JsonResponse(test_procedure_result_list, safe=False)


class UserView(View):
    def get(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.COOKIES.get('auth_token'))
        user=token.user
        profile = UserProfile.objects.get(user=user)
        if not profile.organization:
            return HttpResponse(
                "This user has no organization", status=400
            )
        
        organization = profile.organization
        users = UserProfile.objects.filter(organization=organization)

        user_list = []

        for user_profile in users:
            related_user = user_profile.user
            user_data = {
                "id": user_profile.id,
                "email": related_user.email,
                "first_name":related_user.first_name,
                "last_name":related_user.last_name,
                "role": user_profile.role,
                "organization_id": user_profile.organization_id
            }

            user_list.append(user_data)

        return JsonResponse(user_list, safe=False)

class CreateProjectView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        token = Token.objects.get(key=request.COOKIES.get('auth_token'))
        profile = UserProfile.objects.get(user=token.user)
        
        if profile.organization != None:
            organization = profile.organization
    
        else:
            return HttpResponse(
                "This user has no organization", status=400
            )
        
        project = Project.objects.create(
                organization=organization,
                name=data.get("name"),
                description=data.get("description"),
        )

        return HttpResponse(
                "created", status=201
        )