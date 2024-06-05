import json
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Organization, UserProfile, Roles, Token, OrganizationInvite
from datetime import datetime, timedelta
from rest_framework import status


class TestViews(TestCase):
    def setUp(self):
        # Clean up any existing UserProfile instances to avoid duplicates
        UserProfile.objects.all().delete()

        self.client = Client()
        self.user = User.objects.create(first_name="first_name",
                                        last_name="last_name",
                                        username='testuser',
                                        email='test@example.com')
        self.user.set_password("testpassword")
        self.user.save()
        self.user2 = User.objects.create(first_name="first_name2",
                                         last_name="last_name2",
                                         username='testuser2',
                                         email='invite@example.com')
        self.user2.set_password("testpassword2")
        self.user2.save()
        self.token = Token.objects.create(user=self.user, key='auth_token')
        self.organization = Organization.objects.create(name='Test Organization')

        profile = UserProfile.objects.get(user=self.user)
        profile.organization = self.organization
        profile.role = Roles.ORGANIZATION_LEADER
        profile.save()

        self.invite_hash = 'test_invite_hash'
        self.invite = OrganizationInvite.objects.create(organization=self.organization, user=self.user,
                                                        hash=self.invite_hash)

    def test_login_view(self):
        url = reverse('organizations:login')
        response = self.client.post(url, {'username': 'testuser', 'password': 'testpassword'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('auth_token', response.cookies)
        self.assertTrue(Token.objects.filter(user=self.user).exists())

    def test_signup_view(self):
        url = reverse('organizations:register')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'newuser@example.com',
            'password': 'newuserpassword',
            'organization_name': 'New Organization'
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('auth_token', response.cookies)
        self.assertTrue(User.objects.filter(email='newuser@example.com').exists())
        self.assertTrue(UserProfile.objects.filter(user__email='newuser@example.com').exists())
        self.assertTrue(Organization.objects.filter(name='New Organization').exists())

    def test_user_invite_view(self):
        url = reverse('organizations:user_invite')
        self.client.cookies['auth_token'] = self.token.key  # Setting the auth token in cookies for authentication
        data = {'email': 'invite@example.com'}
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(OrganizationInvite.objects.filter(organization=self.organization, user=self.user).exists())
