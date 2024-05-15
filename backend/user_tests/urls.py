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
from .views import TestView, TestProcedureView, TestProcedureDetailView, TestProcedureResultListView, TestProcedureResultDetailView, UserView, CreateProjectView, DeleteProjectView, DeleteTestView

app_name = 'user_tests'
urlpatterns = [
    path('users/', UserView.as_view(), name='user_view'), # Done
    path('projects/<int:pk>/tests/', TestView.as_view(), name='test_view'), # Done

    path('projects/<int:pk>/testprocedures/', TestProcedureView.as_view(), name='test_procedure_view'), # Done
    path('projects/<int:pk>/testprocedures/<int:procedure_id>/', TestProcedureDetailView.as_view(), name='test_procedure_detail_view'), # Done

    path('projects/<int:pk>/testprocedures/', TestProcedureView.as_view(), name='test_procedure_view'),
    path('projects/<int:pk>/testprocedureresults/', TestProcedureResultListView.as_view(), name='test_procedure_results_view'),
    path('projects/<int:pk>/testprocedureresults/<int:procedure_id>/results/<int:result_id>/', TestProcedureResultDetailView.as_view(), name='test_procedure_results_view'),

    path('projects/<int:pk>/testprocedureresults/<int:procedure_id>/results/', TestProcedureResultListView.as_view(), name='test_procedure_results_view'),

    path('projects/create/', CreateProjectView.as_view(), name='create_project_view'),

    path('projects/<int:pk>/delete', DeleteProjectView.as_view(), name='delete_project_view'),

    path('projects/<int:pk>/tests/<int:test_id>/delete/', DeleteTestView.as_view(), name='delete_test_view'), # Done

]
