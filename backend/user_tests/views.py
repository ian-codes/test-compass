
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


# List Views
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


class TestProcedureDetailView(View):
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
        
        try:
            test_procedure = TestProcedure.objects.get(project=project, pk=kwargs.get('procedure_id'))
        except TestProcedure.DoesNotExist:
            return HttpResponse(
                "TestProcedure with pk does not exist", status=400
            )     
        
        test_procedure_tests = []


        for test in test_procedure.acceptance_tests.all():
            test_procedure_tests.append(
                {
                    'creator': test.creator.id if test.creator else '',
                    'project': test.project.id,
                    'name': test.name,
                    'description': test.description,
                    'pre_conditions': test.pre_conditions,
                    'steps': test.steps,
                    'expected_result': test.expected_result,
                    'created_at':test.created_at,

                }
            )

        test_procedure_json = {
            'created_at': test_procedure.created_at,
            'name':test_procedure.name,
            'description':test_procedure.description,
            'project':test_procedure.project.id,
            'tests':test_procedure_tests
        }


   
        
        return JsonResponse(test_procedure_json, safe=False)


class TestProcedureResultListView(View):
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
        test_procedure_results = TestProcedureResult.objects.filter(test_procedure__project=project)

        test_procedure_result_list = []
        for result in test_procedure_results:
            result_data = {
                'id': result.id,
                'creator': {
                    "username":result.creator.username,
                    "first_name":result.creator.first_name,
                    "last_name":result.creator.last_name,
                },
                'created_at': result.created_at,
                'test_procedure': result.test_procedure.id
            }
            test_procedure_result_list.append(result_data)

        return JsonResponse(test_procedure_result_list, safe=False)
    
class TestProcedureResultDetailView(View):
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

        try:
            test_procedure_result = TestProcedureResult.objects.get(test_procedure__project=project, pk=kwargs.get('result_id'))
        except TestProcedureResult.DoesNotExist:
            return HttpResponse(
                "No procedure result found", status=400
            )
        
        acceptance_test_result_list = []
        for acceptance_test_result in test_procedure_result.useracceptancetestresult_set.all():
            acceptance_test = {
                'created_at': acceptance_test_result.created_at,
                'status': acceptance_test_result.status,
                'notes': acceptance_test_result.notes,
                'acceptance_test': {
                    'test_name':  acceptance_test_result.acceptance_test.name,
                    'test_description':  acceptance_test_result.acceptance_test.description,
                    'test_pre_conditions':  acceptance_test_result.acceptance_test.pre_conditions,
                    'test_expected_result':  acceptance_test_result.acceptance_test.expected_result,
                    'test_expected_steps':  acceptance_test_result.acceptance_test.steps,
                }  

            }
            acceptance_test_result_list.append(acceptance_test)
            
        test_procedure_json = {
            'created_at': test_procedure_result.created_at,
            'creator': {
                    "username":test_procedure_result.creator.username,
                    "first_name":test_procedure_result.creator.first_name,
                    "last_name":test_procedure_result.creator.last_name,
            },
            'acceptance_test_results':acceptance_test_result_list

        }

        return JsonResponse(test_procedure_json, safe=False)




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

# Create Views
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


# Delete Views
class DeleteProjectView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.COOKIES.get('auth_token'))
        user = token.user
        profile = UserProfile.objects.get(user=user)
        pk = kwargs.get('pk')
        if not profile.organization:
            return HttpResponse(
                "This user has no organization", status=400
            )
        project = None
        try:
            project = Project.objects.get(pk=pk)

        except Project.DoesNotExist:
            return HttpResponse(
                "Project with pk does not exist", status=400
            )

        if not user in project.user_list.all():
            return HttpResponse(
                "Unauthorized", status=403
            )
        project.delete()

        return HttpResponse(
            "deleted", status=200
        )

class DeleteTestView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.COOKIES.get('auth_token'))
        user = token.user
        profile = UserProfile.objects.get(user=user)
        pk = kwargs.get('pk')
        test_id = kwargs.get('test_id')
        if not profile.organization:
            return HttpResponse(
                "This user has no organization", status=400
            )
        project = None
        try:
            project = Project.objects.get(pk=pk)

        except Project.DoesNotExist:
            return HttpResponse(
                "Project with pk does not exist", status=400
            )

        if not user in project.user_list.all():
            return HttpResponse(
                "Unauthorized", status=403
            )

        test = UserAcceptanceTest.objects.get(pk=test_id)
        test.delete()

        return HttpResponse(
            "deleted", status=200
        )