# tests.py
import json
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from organizations.models import Organization, UserProfile, Token, Roles
from .models import Project, UserAcceptanceTest, TestProcedure, TestProcedureResult, UserAcceptanceTestResult


class ViewTests(TestCase):

    def setUp(self):
        # Clean up any existing UserProfile instances to avoid duplicates
        UserProfile.objects.all().delete()

        # Create User, Organization, UserProfile, Token, Project, etc.
        self.client = Client()

        self.organization = Organization.objects.create(name="Test Org")

        self.user = User.objects.create(
            first_name="first_name",
            last_name="last_name",
            email="email",
            username="username",

        )
        self.user.set_password("password")
        self.user.save()
        #self.user_profile = UserProfile.objects.create(user=self.user, organization=self.organization)
        profile = UserProfile.objects.get(user=self.user)
        profile.organization = self.organization
        profile.role = Roles.ORGANIZATION_LEADER
        profile.save()
        self.token = Token.objects.create(user=self.user, key='auth_token')

        self.project = Project.objects.create(organization=self.organization, name="Test Project",
                                              description="Test Description")
        self.project.user_list.add(self.user)

        self.test_procedure = TestProcedure.objects.create(project=self.project, name="Test Procedure",
                                                           description="Procedure Description")
        self.user_acceptance_test = UserAcceptanceTest.objects.create(
            creator=self.user, project=self.project, name="Acceptance Test",
            description="Test Description", pre_conditions="Pre Conditions",
            steps="Steps", expected_result="Expected Result"
        )

        self.test_procedure.acceptance_tests.add(self.user_acceptance_test)
        self.test_procedure_result = TestProcedureResult.objects.create(test_procedure=self.test_procedure,
                                                                        creator=self.user)
        self.user_acceptance_test_result = UserAcceptanceTestResult.objects.create(
            test_procedure_result=self.test_procedure_result, acceptance_test=self.user_acceptance_test,
            status='PENDING', notes="Notes"
        )

    def test_test_view(self):
        self.client.cookies['auth_token'] = self.token.key
        response = self.client.get(reverse('user_tests:test_view', kwargs={'pk': self.project.pk}))
        self.assertEqual(response.status_code, 200)

    def test_test_procedure_detail_view(self):
        self.client.cookies['auth_token'] = self.token.key
        response = self.client.get(reverse('user_tests:test_procedure_detail_view',
                                           kwargs={'pk': self.project.pk, 'procedure_id': self.test_procedure.pk}))
        self.assertEqual(response.status_code, 200)

    def test_test_procedure_result_list_view(self):
        self.client.cookies['auth_token'] = self.token.key
        response = self.client.get(reverse('user_tests:test_procedure_results_view', kwargs={'pk': self.project.pk}))
        self.assertEqual(response.status_code, 200)

    def test_test_procedure_result_detail_view(self):
        self.client.cookies['auth_token'] = self.token.key
        response = self.client.get(reverse('user_tests:test_procedure_results_detail_view',
                                           kwargs={'pk': self.project.pk, 'result_id': self.test_procedure_result.pk}))
        self.assertEqual(response.status_code, 200)

    def test_test_procedures_view(self):
        self.client.cookies['auth_token'] = self.token.key
        response = self.client.get(reverse('user_tests:test_procedure_view', kwargs={'pk': self.project.pk}))
        self.assertEqual(response.status_code, 200)

    def test_projects_view(self):
        self.client.cookies['auth_token'] = self.token.key
        response = self.client.get(reverse('user_tests:user_view'))
        self.assertEqual(response.status_code, 200)

    def test_project_view(self):
        self.client.cookies['auth_token'] = self.token.key
        response = self.client.get(reverse('user_tests:project_details_view', kwargs={'project_id': self.project.pk}))
        self.assertEqual(response.status_code, 200)

    def test_user_view(self):
        self.client.cookies['auth_token'] = self.token.key
        response = self.client.get(reverse('user_tests:user_view'))
        self.assertEqual(response.status_code, 200)

    def test_users_view(self):
        self.client.cookies['auth_token'] = self.token.key
        response = self.client.get(reverse('user_tests:users_view'))
        self.assertEqual(response.status_code, 200)

    def test_create_project_view(self):
        self.client.cookies['auth_token'] = self.token.key
        data = {
            'name': 'New Project',
            'description': 'New Description'
        }
        response = self.client.post(reverse('user_tests:create_project_view'), data=json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_test_view(self):
        self.client.cookies['auth_token'] = self.token.key
        data = {
            'name': 'New Test',
            'description': 'Test Description',
            'pre_conditions': 'Pre Conditions',
            'steps': 'Steps',
            'expected_result': 'Expected Result'
        }
        response = self.client.post(reverse('user_tests:create_test_view', kwargs={'pk': self.project.pk}),
                                    data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_test_procedure_view(self):
        self.client.cookies['auth_token'] = self.token.key
        data = {
            'name': 'New Test Procedure',
            'description': 'Procedure Description',
            'acceptance_tests': [self.user_acceptance_test.pk]
        }
        response = self.client.post(reverse('user_tests:create_test_procedure_view', kwargs={'pk': self.project.pk}),
                                    data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_test_procedure_result_view(self):
        self.client.cookies['auth_token'] = self.token.key
        data = {
            'tests': [{
                'id': self.user_acceptance_test.pk,
                'status': 'SUCCESS',
                'notes': 'Notes'
            }]
        }
        response = self.client.post(reverse('user_tests:create_test_procedure_result_view',
                                            kwargs={'pk': self.project.pk, 'procedure_id': self.test_procedure.pk}),
                                    data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_delete_project_view(self):
        self.client.cookies['auth_token'] = self.token.key
        response = self.client.delete(reverse('user_tests:delete_project_view', kwargs={'pk': self.project.pk}))
        self.assertEqual(response.status_code, 200)

    def test_delete_test_view(self):
        self.client.cookies['auth_token'] = self.token.key
        response = self.client.delete(reverse('user_tests:delete_test_view',
                                              kwargs={'pk': self.project.pk, 'test_id': self.user_acceptance_test.pk}))
        self.assertEqual(response.status_code, 200)

    def test_delete_test_procedure_view(self):
        self.client.cookies['auth_token'] = self.token.key
        response = self.client.delete(reverse('user_tests:delete_test_procedure_view',
                                              kwargs={'pk': self.project.pk, 'procedure_id': self.test_procedure.pk}))
        self.assertEqual(response.status_code, 200)

    def test_delete_test_procedure_results_view(self):
        self.client.cookies['auth_token'] = self.token.key
        response = self.client.delete(reverse('user_tests:delete_test_procedure_result_view',
                                              kwargs={'pk': self.project.pk,
                                                      'result_id': self.test_procedure_result.pk}))
        self.assertEqual(response.status_code, 200)

    def test_delete_acceptance_test_results_view(self):
        self.client.cookies['auth_token'] = self.token.key
        response = self.client.delete(reverse('user_tests:delete_test_result_view', kwargs={'pk': self.project.pk,
                                                                                            'result_id': self.user_acceptance_test_result.pk}))
        self.assertEqual(response.status_code, 200)
