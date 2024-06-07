from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.authtoken.views import obtain_auth_token
from .views import SignupView, UserInviteView, OrgInvitationView, LoginView, LogoutView

"""
    URL-Patterns for API-Endpoint. Each url shows to a view in (organizations.views.py)
"""
app_name = 'organizations'
urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('account/login/',LoginView.as_view(),name="login"),
    path('account/logout/',LogoutView.as_view(),name="logout"),
    path('account/register/', SignupView.as_view(), name='register'),
    path('organization/invite/', UserInviteView.as_view(), name='user_invite'),
    path('organization/<int:pk>/invite/<str:hash>/', OrgInvitationView.as_view(), name='organization_invite'),]
