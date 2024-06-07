
import json
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, ListView, TemplateView, CreateView, DetailView
from django.http import JsonResponse, HttpResponse, Http404
from .models import UserAcceptanceTest, UserAcceptanceTestResult, TestProcedureResult, TestProcedure, User, Project
from organizations.models import UserProfile, Organization, Token

# List Views

class OrganizationView(View):
    def get(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.COOKIES.get('auth_token'))
        user=token.user
        profile = UserProfile.objects.get(user=user)
        if not profile.organization:
            return HttpResponse(
                "This user has no organization", status=400
            )
        
        organization = Organization.objects.get(id=profile.organization.id)

        organization_json = {
            'name': organization.name
        }

        return JsonResponse(organization_json, safe=False)


class TestsView(View):
    """
    A list of acceptancetests :model:`user_tests.UserAcceptanceTest` as JSON.

    **Return-Value**

    ``test_list``
        An list of :model:`user_tests.UserAcceptanceTest` instances.

    **Parameters:**
    - 'pk': Primary key of project of which the tests should be returned
   
    """
    def get(self, request, *args, **kwargs):
        """
            Gets JWT-Token from request cookies and checks if they exist in the database
        """
        token = Token.objects.get(key=request.COOKIES.get('auth_token'))
        user=token.user
        profile = UserProfile.objects.get(user=user)

        """
            Checks wether user is part of an organization (:model:`organizations.Organization)
        """
        if not profile.organization:
            return HttpResponse(
                "This user has no organization", status=400
            )
        project = None
        """
            Checks wether project (:model:`user_tests.Project`) with id passed in URL exists
        """
        try:    
            project = Project.objects.get(pk=kwargs.get('pk'))        

        except Project.DoesNotExist:
          return HttpResponse(
                "Project with pk does not exist", status=400
            )        
        """
            Checks wether user (:model:`auth.User`) is associated with project (:model:`user_tests.Project`) with id passed in URL
        """
        if not user in project.user_list.all():
            return HttpResponse(
                "Unauthorized", status=403
            )        

        tests = UserAcceptanceTest.objects.filter(project=project)
        test_list = list(tests.values())

        return JsonResponse(test_list, safe=False)


class TestProcedureDetailView(View):
    """
    A certain testprocedure (:model:`user_tests.TestProcedure`) with associated tests (:model:`user_tests.UserAcceptanceTest`) .

    **Return-Value**

    ``test_procedure_json``
        A json of :model:`user_tests.UserAcceptanceTest` instances.

    **Parameters:**
    - 'pk': Primary key of project of the test procedure
    - 'procedure_id': Primary key of procedure to get
    """
    def get(self, request, *args, **kwargs):
        """
            Repetitive Code to check for permission, check doc of TestView to gain more information
        """
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
        
        """
            Gets TestProcedure with procedure_id from key-word-arguments (kwargs)
        """
        try:
            test_procedure = TestProcedure.objects.get(project=project, pk=kwargs.get('procedure_id'))
        except TestProcedure.DoesNotExist:
            return HttpResponse(
                "TestProcedure with pk does not exist", status=400
            )     
        
        test_procedure_tests = []

        """
            Adds each test (:model:`user_tests.UserAcceptanceTest`) in the list of tests 
        """
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
    """
    A list of testprocedure results (:model:`user_tests.TestProcedureResult`).

    **Return-Value**

    ``test_procedure_result_list``
        A list of testprocedure results(:model:`user_tests.TestProcedureResult`) as JSON.

    **Parameters:**
    - 'pk': Primary key of project of which the procedure results should be returned
    """
    def get(self, request, *args, **kwargs):

        """
            Repetitive Code to check for permission, check doc of TestView to gain more information
        """
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
    """
    Details of testprocedure result (:model:`user_tests.TestProcedureResult`) with associated testresults (:model:`user_tests.UserAcceptanceTest`) .

    **Return-Value**

    ``test_procedure_json``
        A JSON with TestProcedureResult results(:model:`user_tests.TestProcedureResult`),.

    **Parameters:**
    - 'pk': Primary key of project of which the procedure result should be returned
    - 'result_id': Primary key of procedure result to get
    """
    def get(self, request, *args, **kwargs):
        """
            Repetitive Code to check for permission, check doc of TestView to gain more information
        """
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


class TestResultDetailView(View):
    """
    Details of testprocedure result (:model:`user_tests.TestProcedureResult`) with associated testresults (:model:`user_tests.UserAcceptanceTest`) .

    **Return-Value**

    ``test_result_json``
        A JSON with UserAcceptanceTestResult (:model:`user_tests.UserAcceptanceTestResult`),.

    **Parameters:**
    - 'pk': Primary key of project of which the procedure result should be returned
    - 'result_id': Primary key of procedure result to get
    """
    def get(self, request, *args, **kwargs):
        """
            Repetitive Code to check for permission, check doc of TestView to gain more information
        """
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
            test_result = UserAcceptanceTestResult.objects.get(pk=kwargs.get('result_id'))
        except TestProcedureResult.DoesNotExist:
            return HttpResponse(
                "No procedure result found", status=400
            )
             
        test_result_json = {
            'created_at': test_result.created_at,
            'status': test_result.status,
            'notes': test_result.notes,
            'acceptance_test': {
                    'test_name':  test_result.acceptance_test.name,
                    'test_description':  test_result.acceptance_test.description,
                    'test_pre_conditions':  test_result.acceptance_test.pre_conditions,
                    'test_expected_result':  test_result.acceptance_test.expected_result,
                    'test_expected_steps':  test_result.acceptance_test.steps,
            }  

        }

        return JsonResponse(test_result_json, safe=False)


class TestProceduresView(View):
    """
    List of testprocedures (:model:`user_tests.TestProcedure`)

    **Return-Value**

    ``test_procedure_list``
        A list with TestProcedures (:model:`user_tests.TestProcedure`),.

    **Parameters:**
    - 'pk': Primary key of project of which the procedures should be returned
    """
    def get(self, request, *args, **kwargs):
        """
            Repetitive Code to check for permission, check doc of TestView to gain more information
        """
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
        
        if not user in project.user_list.all() and profile.organization != project.organization:
            return HttpResponse(
                "Unauthorized", status=403
            )
        test_procedures = TestProcedure.objects.filter(project=project)

        test_procedure_list = list(test_procedures.values())

        return JsonResponse(test_procedure_list, safe=False)


class ProjectsView(View):
    """
    List of projects in organization (:model:`user_tests.Projects`)

    **Return-Value**

    ``list(projects.values())``
        A List of projects (:model:`user_tests.Projects`) as JSON.

    **Parameters:**

    """
    def get(self, request, *args, **kwargs):
        """
            Repetitive Code to check for permission, check doc of TestView to gain more information
        """
        token = Token.objects.get(key=request.COOKIES.get('auth_token'))
        user=token.user
        profile = UserProfile.objects.get(user=user)
        if not profile.organization:
            return HttpResponse(
                "This user has no organization", status=400
            )
        
        organization = profile.organization
        projects = Project.objects.filter(organization=organization)
        return JsonResponse(list(projects.values()), safe=False)


class ProjectView(View):
    """
    Details of project (:model:`user_tests.Projects`) as JSON

    **Return-Value**

    ``project_json``
        A project (:model:`user_tests.Projects`) as JSON.

    **Parameters:**
    - 'pk': Primary key of project which should be returned
    """
    def get(self, request, project_id, *args, **kwargs):
        """
            Repetitive Code to check for permission, check doc of TestView to gain more information
        """
        token = Token.objects.get(key=request.COOKIES.get('auth_token'))
        user=token.user
        profile = UserProfile.objects.get(user=user)
        if not profile.organization:
            return HttpResponse(
                "This user has no organization", status=400
            )
        
        organization = profile.organization

        try:
            project = Project.objects.get(id=project_id)
            if project.organization != organization:
                return HttpResponse("Not authorized to view this project", status=403)
            
            project_json = {
                'id': project.id,
                'name': project.name,
                'description': project.description,
                'created_at': project.created_at
            }

            return JsonResponse(project_json, content_type='application/json', safe=False)
        except Project.DoesNotExist:
            return HttpResponse("Project not found", status=404)


class UserView(View):
    """
    Details of User (:model:`auth.User`) as JSON

    **Return-Value**

    ``user_json``
        Requesting User (:model:`auth.User`) as JSON.

    **Parameters:**
    - 'auth_token': JWT-Authorization-Token passed as http-only-cookie
    """
    def get(self, request, *args, **kwargs):
        """
            Repetitive Code to check for permission, check doc of TestView to gain more information
        """
        token = Token.objects.get(key=request.COOKIES.get('auth_token'))
        user=token.user
        profile = UserProfile.objects.get(user=user)
        if not profile.organization:
            return HttpResponse(
                "This user has no organization", status=400
            )

        user_json = {
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": profile.role,
            "organization_id": profile.organization.id
        }

        return JsonResponse(user_json, safe=False)


class UsersView(View):
    """
    List of Users (:model:`auth.User`) in organization as JSON

    **Return-Value**

    ``user_list``
        List of Users (:model:`auth.User`) as JSON.

    **Parameters:**
    - 'auth_token': JWT-Authorization-Token passed as http-only-cookie
    """
    def get(self, request, *args, **kwargs):
        """
            Repetitive Code to check for permission, check doc of TestView to gain more information
        """
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
    """
        Checks for csrf_token to prevent cross-site-request-forgery
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    """
    Endpoint to create of Project (:model:`user_tests.Project`)

    **Body**
    {
        "name": <str:project-name>,
        "description": <str:project-description>,
        "users": <list[int]:user-ids>
    }

    **Return-Value**

    ``Status: 201 - Created``

    **Parameters:**
    - 'auth_token': JWT-Authorization-Token passed as http-only-cookie
    """
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        """
            Repetitive Code to check for permission, check doc of TestView to gain more information
        """
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

        # for id in data.get("users"):
        #     try:
        #         user = User.objects.get(pk=id)
        #         project.user_list.add(user)
        #     except User.DoesNotExist:
        #         return HttpResponse(
        #         "User doesn't exist", status=400
        #         )

        return HttpResponse(
                "created", status=201
        )

class CreateTestView(View):
    """
        Checks for csrf_token to prevent cross-site-request-forgery
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    """
    Endpoint to create Acceptance Test (:model:`user_tests.UserAcceptanceTest`)

    **Body**
    {
        "name": <str:name>,
        "description": <str:description>,
        "pre_conditions": <str:coditions>,
        "steps": <str:steps>,
        "expected_result": <str:result>
    }

    **Return-Value**

    ``Status: 201 - Created``

    **Parameters:**
    - 'auth_token': JWT-Authorization-Token passed as http-only-cookie
    - 'pk': Primary key of project in which test should be created

    """
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

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
        
        if not user in project.user_list.all() and profile.organization != project.organization:
            return HttpResponse(
                "Unauthorized", status=403
            )

        
        acceptance_test = UserAcceptanceTest.objects.create(
                creator=token.user,
                project=project,
                name=data.get("name"),
                description=data.get("description"),
                pre_conditions=data.get("pre_conditions"),
                steps=data.get("steps"),
                expected_result=data.get("expected_result"),
        )

        return HttpResponse(
                "created", status=201
        )

class CreateTestProcedureView(View):
    """
        Checks for csrf_token to prevent cross-site-request-forgery
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    """
    Endpoint to create TestProcedure (:model:`user_tests.TestProcedure`)

    **Body**
    {
        "name": <str:name>,
        "description": <str:description>,
        "acceptance_tests": <list[int]:test-ids>
    }

    **Return-Value**

    ``Status: 201 - Created``

    **Parameters:**
    - 'auth_token': JWT-Authorization-Token passed as http-only-cookie
    - 'pk': Primary key of project in which procedure should be created

    """
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

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
        
        if not user in project.user_list.all() and profile.organization != project.organization:
            return HttpResponse(
                "Unauthorized", status=403
            )

        test_procedure = TestProcedure(
                project=project,
                name=data.get("name"),
                description=data.get("description"),
        )

        test_procedure.save()

        if data.get("acceptance_tests") is not None:
            for id in data.get("acceptance_tests"):
                try:
                    test = UserAcceptanceTest.objects.get(pk=id)
                    test_procedure.acceptance_tests.add(test)
                except UserAcceptanceTest.DoesNotExist:
                    return HttpResponse(
                    "UserAcceptanceTest doesn't exist", status=400
                )

        
        test_procedure.save()

        return HttpResponse(
                "created", status=201
        )

class CreateTestProcedureResultView(View):
    """
        Checks for csrf_token to prevent cross-site-request-forgery
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    """
    Endpoint to create TestProcedure result (:model:`user_tests.TestProcedureResult`)

    **Body**
    {
        "tests": [
            {
                "id": <int:test-id>,
                "status": <str:status>,
                "notes": <str:notes>
            }
        ] 
    }

    **Return-Value**

    ``Status: 201 - Created``

    **Parameters:**
    - 'auth_token': JWT-Authorization-Token passed as http-only-cookie
    - 'pk': Primary key of project in which procedure result should be created
    - 'procedure_id': Primary key of procedure for which result should be created

    """
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

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
        
        procedure = TestProcedure.objects.get(pk=kwargs.get('procedure_id'))
        test_procedure_result = TestProcedureResult.objects.create(test_procedure=procedure, creator=token.user)
        test_procedure_result.save()

        for test in data.get("tests", []):
            try:
                acceptance_test = UserAcceptanceTest.objects.get(pk=test.get("id"), project=project)
                if acceptance_test in procedure.acceptance_tests.all():
                    test_result = UserAcceptanceTestResult.objects.create(
                        test_procedure_result=test_procedure_result,
                        acceptance_test=acceptance_test,
                        status = test.get("status"),
                        notes = test.get("notes"),
                    )
            except UserAcceptanceTest.DoesNotExist:
                return HttpResponse(
                    # f"UserAcceptanceTest with id  is not in this procedure", status=400
                )
                
        return HttpResponse(
                "created", status=201
        )
    
class CreateTestResultView(View):
    """
        Checks for csrf_token to prevent cross-site-request-forgery
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    """
    Endpoint to create TestProcedure result (:model:`user_tests.TestProcedureResult`)

    **Body**
            {
                "id": <int:test-id>,
                "status": <str:status>,
                "notes": <str:notes>
            }

    **Return-Value**

    ``Status: 201 - Created``

    **Parameters:**
    - 'auth_token': JWT-Authorization-Token passed as http-only-cookie
    - 'pk': Primary key of project in which procedure result should be created

    """
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

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
            acceptance_test = UserAcceptanceTest.objects.get(id=data.get('test_id'), project=project)
        except UserAcceptanceTest.DoesNotExist:
            return HttpResponse(
                "Test does not exist or is not in your project", status=400
            )
        try:
            result = UserAcceptanceTestResult.objects.create(
                status=data.get('status'),
                notes=data.get('notes'),
                acceptance_test = acceptance_test
            )
        except:
            return HttpResponse(
                "Something went wrong", status=400
            )
        return HttpResponse(
                "created", status=201
            )

# Delete Views
class DeleteProjectView(View):
    """
        Checks for csrf_token to prevent cross-site-request-forgery
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    """
    Endpoint to delete project (:model:`user_tests.Project`)


    **Return-Value**

    ``Status: 200 - Deleted``

    **Parameters:**
    - 'auth_token': JWT-Authorization-Token passed as http-only-cookie
    - 'pk': Primary key of project which should be deleted

    """
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

    """
        Checks for csrf_token to prevent cross-site-request-forgery
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    """
    Endpoint to delete test (:model:`user_tests.UserAcceptanceTest`)


    **Return-Value**

    ``Status: 200 - Deleted``

    **Parameters:**
    - 'auth_token': JWT-Authorization-Token passed as http-only-cookie
    - 'pk': Primary key of project 
    - 'test_id': Primary key of test which should be deleted

    """
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
    
class DeleteTestProcedureView(View):
    """
        Checks for csrf_token to prevent cross-site-request-forgery
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    """
    Endpoint to delete test procedure (:model:`user_tests.TestProcedure`)


    **Return-Value**

    ``Status: 200 - Deleted``

    **Parameters:**
    - 'auth_token': JWT-Authorization-Token passed as http-only-cookie
    - 'pk': Primary key of project in which procedure should be deleted
    - 'procedure_id': Primary key of procedure which should be deleted

    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.COOKIES.get('auth_token'))
        user = token.user
        profile = UserProfile.objects.get(user=user)
        pk = kwargs.get('pk')
        procedure_id = kwargs.get('procedure_id')
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

        procedure = TestProcedure.objects.get(pk=procedure_id)
        procedure.delete()

        return HttpResponse(
            "deleted", status=200
        )
    
class DeleteTestProcedureResultsView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.COOKIES.get('auth_token'))
        user = token.user
        profile = UserProfile.objects.get(user=user)
        pk = kwargs.get('pk')
        result_id = kwargs.get('result_id')
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

        result = TestProcedureResult.objects.get(pk=result_id)
        result.delete()

        return HttpResponse(
            "deleted", status=200
        )

class DeleteAcceptanceTestResultsView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.COOKIES.get('auth_token'))
        user = token.user
        profile = UserProfile.objects.get(user=user)
        pk = kwargs.get('pk')
        result_id = kwargs.get('result_id')
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

        result = UserAcceptanceTest.objects.get(pk=result_id)
        result.delete()

        return HttpResponse(
            "deleted", status=200
        )