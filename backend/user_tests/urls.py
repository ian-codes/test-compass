"""
URL configuration for testcompass_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from .views import ProjectView, UserView, TestView, TestProceduresView, TestProcedureDetailView, TestProcedureResultListView, TestProcedureResultDetailView, UsersView, CreateProjectView, DeleteProjectView, DeleteTestView, CreateTestView, CreateTestProcedureView, CreateTestProcedureResultView, ProjectsView, DeleteTestProcedureView, DeleteTestProcedureResultsView, DeleteAcceptanceTestResultsView

app_name = 'user_tests'
urlpatterns = [
    path('projects/', ProjectsView.as_view(), name='user_view'), # Done
    path('projects/<int:project_id>/', ProjectView.as_view(), name='project_details_view'),


    path('users/', UsersView.as_view(), name='users_view'), # Done
    path('user/', UserView.as_view(), name='user_view'),

    path('projects/<int:pk>/tests/', TestView.as_view(), name='test_view'), # Done

    path('projects/<int:pk>/testprocedures/', TestProceduresView.as_view(), name='test_procedure_view'), # Done
    path('projects/<int:pk>/testprocedures/<int:procedure_id>/', TestProcedureDetailView.as_view(), name='test_procedure_detail_view'), # Done

    path('projects/<int:pk>/testprocedureresults/', TestProcedureResultListView.as_view(), name='test_procedure_results_view'), # Done 
    path('projects/<int:pk>/testprocedureresults/<int:result_id>/', TestProcedureResultDetailView.as_view(), name='test_procedure_results_detail_view'), # Done

    path('projects/create/', CreateProjectView.as_view(), name='create_project_view'), # Done
    path('projects/<int:pk>/tests/create/', CreateTestView.as_view(), name='create_test_view'),# Done
    path('projects/<int:pk>/testprocedures/create/', CreateTestProcedureView.as_view(), name='create_test_procedure_view'), # Done
    path('projects/<int:pk>/testprocedures/<int:procedure_id>/create/', CreateTestProcedureResultView.as_view(), name='create_test_procedure_result_view'), # Done


    path('projects/<int:pk>/delete', DeleteProjectView.as_view(), name='delete_project_view'), # Done

    path('projects/<int:pk>/tests/<int:test_id>/delete/', DeleteTestView.as_view(), name='delete_test_view'), # Done
    path('projects/<int:pk>/testprocedures/<int:procedure_id>/delete/', DeleteTestProcedureView.as_view(), name='delete_test_procedure_view'), # Done
    path('projects/<int:pk>/testprocedureresults/<int:result_id>/delete/', DeleteTestProcedureResultsView.as_view(), name='delete_test_procedure_result_view'), # Done
    path('projects/<int:pk>/testresults/<int:result_id>/delete/', DeleteAcceptanceTestResultsView.as_view(), name='delete_test_result_view'), # Done

]
