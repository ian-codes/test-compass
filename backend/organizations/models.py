from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings  
from django.dispatch import receiver
from rest_framework.authtoken.models import Token 
class UserRole(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, verbose_name="Name")
    description = models.TextField(verbose_name="Beschreibung", blank=True, null=True, max_length=250)


    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Benutzer",
        on_delete=models.CASCADE)

    role = models.ForeignKey(
        UserRole,
        verbose_name="Rolle",
        on_delete=models.SET_NULL, null=True, blank=True)

    organization = models.ForeignKey(
        "Organization",
        verbose_name="Organisation",
        on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.user.username


class Organization(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, verbose_name="Name")



def create_user_profile(sender, instance, created, **kwargs):  
    if created: 
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)