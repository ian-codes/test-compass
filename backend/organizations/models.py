from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings  
from django.dispatch import receiver
from rest_framework.authtoken.models import Token 
from datetime import datetime, timedelta
class Roles(models.TextChoices):
    ORGANIZATION_LEADER = "unternehmensleiter", "Unternehmensleiter"
    EMPLOYEE = "mitarbeiter", "Mitarbeiter"


class UserProfile(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Benutzer",
        on_delete=models.CASCADE)

    role = models.CharField(max_length=40, blank=True, null=True, choices=Roles.choices, verbose_name="Benutzerrolle")


    organization = models.ForeignKey(
        "Organization",
        verbose_name="Organisation",
        on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}"


class Organization(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, verbose_name="Name")
    def __str__(self):
        return f"{self.name}"


class OrganizationInvite(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True, related_name="rental_invite")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="rental_invite")

    expired_on = models.DateTimeField(null=True, blank=True, default=datetime.today() + timedelta(days=30))
    hash = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)




def create_user_profile(sender, instance, created, **kwargs):  
    if created: 
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)