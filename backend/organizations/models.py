from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings  
from django.dispatch import receiver
from datetime import datetime, timedelta

"""
    Stores the available roles a user can have inside the organizatiton
"""
class Roles(models.TextChoices):
    ORGANIZATION_LEADER = "unternehmensleiter", "Unternehmensleiter"
    EMPLOYEE = "mitarbeiter", "Mitarbeiter"


"""
    Stores the JWT-Auth-Token of the user for the authentication over the frontend
"""
class Token(models.Model):
    key = models.CharField("Key", max_length=512, primary_key=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)

"""
    Stores additional information about the default django user (:model:`auth.User`). This
    model associates the user to an organization (:model:`organizations.Organization`) and a role (:model:`organizations.Role`), 
"""
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
        """
            Returns the username of the associated user (:model:`auth.User`) per default when calling the object
        """
        return f"{self.user.username}"

"""
    Stores the name of the organization
"""
class Organization(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, verbose_name="Name")
    def __str__(self):
        return f"{self.name}"

"""
    Stores the invitation hash to invite a new user (:model:`auth.User`) to an organization. The url for the user to join the
    associated organization (:model:`organizations.Organization`) is generated from the hash.
"""
class OrganizationInvite(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True, related_name="rental_invite")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="rental_invite")

    expired_on = models.DateTimeField(null=True, blank=True, default=datetime.today() + timedelta(days=30))
    hash = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)



"""
    This function created a (:model:`organizations.UserProfile`) instance each time a new user-instance (:model:`auth.User`)
    gets created.
"""
def create_user_profile(sender, instance, created, **kwargs):  
    if created: 
       profile, created = UserProfile.objects.get_or_create(user=instance)  

"""
    Calls the above function everytime when a new user (:model:`auth.User`) is created
"""
post_save.connect(create_user_profile, sender=User) 
