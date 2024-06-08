from django.contrib import admin
from django.urls import include, path, re_path
from .views import OrganizationView, ProjectView, UserView, TestsView, TestProceduresView, TestProcedureDetailView, TestProcedureResultListView, TestProcedureResultDetailView, UsersView, CreateProjectView, DeleteProjectView, DeleteTestView, CreateTestView, CreateTestProcedureView, CreateTestProcedureResultView, ProjectsView, DeleteTestProcedureView, DeleteTestProcedureResultsView, DeleteAcceptanceTestResultsView, CreateTestResultView,TestResultDetailView


"""
    URL-Patterns for API-Endpoint. Each url shows to a view in (user_tests.views.py)
"""
app_name = 'user_tests'
urlpatterns = [
    path('org/', OrganizationView.as_view(), name='organization_view'), # Done

    path('projects/', ProjectsView.as_view(), name='user_view'), # Done
    path('projects/<int:project_id>/', ProjectView.as_view(), name='project_details_view'),

    path('users/', UsersView.as_view(), name='users_view'), # Done
    path('user/', UserView.as_view(), name='user_view'),

    path('projects/<int:pk>/tests/', TestsView.as_view(), name='test_view'), # Done

    path('projects/<int:pk>/procedures/', TestProceduresView.as_view(), name='test_procedure_view'), # Done
    path('projects/<int:pk>/procedures/<int:procedure_id>/', TestProcedureDetailView.as_view(), name='test_procedure_detail_view'), # Done

    path('projects/<int:pk>/procedures/<int:procedure_id>/results/', TestProcedureResultListView.as_view(), name='test_procedure_results_view'), # Done 
    path('projects/<int:pk>/procedures/<int:procedure_id>/results/<int:result_id>/', TestProcedureResultDetailView.as_view(), name='test_procedure_results_detail_view'), # Done

    path('projects/create/', CreateProjectView.as_view(), name='create_project_view'), # Done
    path('projects/<int:pk>/tests/create/', CreateTestView.as_view(), name='create_test_view'),# Done
    path('projects/<int:pk>/procedures/create/', CreateTestProcedureView.as_view(), name='create_test_procedure_view'), # Done
    path('projects/<int:pk>/procedures/<int:procedure_id>/create/', CreateTestProcedureResultView.as_view(), name='create_test_procedure_result_view'), # Done
    path('projects/<int:pk>/tests/<int:test_id>/results/create/', CreateTestResultView.as_view(), name='create_test_procedure_result_view'), # Done


    path('projects/<int:pk>/delete', DeleteProjectView.as_view(), name='delete_project_view'), # Done

    path('projects/<int:pk>/tests/<int:test_id>/delete/', DeleteTestView.as_view(), name='delete_test_view'), # Done
    path('projects/<int:pk>/procedures/<int:procedure_id>/delete/', DeleteTestProcedureView.as_view(), name='delete_test_procedure_view'), # Done
    path('projects/<int:pk>/procedures/results/<int:result_id>/delete/', DeleteTestProcedureResultsView.as_view(), name='delete_test_procedure_result_view'), # Done
    path('projects/<int:pk>/results/<int:result_id>/delete/', DeleteAcceptanceTestResultsView.as_view(), name='delete_test_result_view'), # Done
    path('projects/<int:pk>/results/<int:result_id>/', TestResultDetailView.as_view(), name='test_result_view'), # Done

]
