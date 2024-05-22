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
from rest_framework.authtoken.views import obtain_auth_token
from .views import SignupView, UserInviteView, OrgInvitationView, LoginView, some_protected_view

app_name = 'organizations'
urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('account/login/',LoginView.as_view(),name = "login"),
    path('obj/',some_protected_view, name = "helo"),
    path('account/register/', SignupView.as_view()),
    path('organization/invite/', UserInviteView.as_view()),
    path('organization/<int:pk>/invite/<str:hash>/', OrgInvitationView.as_view(), name='organization_invite'),]
