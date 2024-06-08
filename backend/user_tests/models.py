from django.db import models
from organizations.models import Organization
from django.utils import timezone
from django.contrib.auth.models import User

class TestStatus(models.TextChoices):
    SUCCESS = 'SUCCESS', 'Success'
    FAILED = 'FAILED', "Failed"
    PENDING = 'PENDING', "Pending"


"""
    Stores project details including name and associated 
    :model:`auth.User` as users.
"""
class Project(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name="Organisation", null=False, blank=False)
    name = models.CharField(max_length=150, blank=False, null=False, verbose_name="Name")
    description = models.TextField(verbose_name="Beschreibung", blank=True, null=True, max_length=250)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Erstellt am")
    
    user_list = models.ManyToManyField(
        User, verbose_name="Mitarbeiter der Organisation",
        related_name="project_users",
    )

    def __str__(self):
        """
            Returns the name of the project per default when calling the object
        """
        return self.name

"""
    Stores test information including creator (:model:`auth.User`) and assosciated project (:model:`user_tests.Project`)
"""
class UserAcceptanceTest(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Ersteller", null=True, blank=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Projekt", null=False, blank=False)
    name = models.CharField(max_length=150, blank=False, null=False, verbose_name="Name")
    description = models.TextField(verbose_name="Beschreibung", blank=True, null=True, max_length=250)
    pre_conditions = models.TextField(verbose_name="Vorbedingungen", blank=True, null=True, max_length=500, help_text="Bedingungen vor dem Test")

    steps = models.TextField(verbose_name="Schritte", blank=True, null=True, max_length=500, help_text="Schritte für den Test")

    created_at = models.DateTimeField(default=timezone.now, verbose_name="Erstellt am")

    expected_result = models.TextField(verbose_name="Erwartetes Resultat", blank=True, null=True, max_length=500, help_text="Resultat dass nach dem Test erwartet wird")


    def __str__(self):
        """
            Returns the name of the UserAcceptanceTest per default when calling the object
        """
        return self.name

"""
    Stores test procedure including a list of tests (:model:`user_tests.UserAcceptanceTest`) and assosciated project (:model:`user_tests.Project`)
"""
class TestProcedure(models.Model):
    acceptance_tests = models.ManyToManyField(UserAcceptanceTest, null=True, blank=True)
    name = models.CharField(max_length=150, blank=False, null=False, verbose_name="Name")
    description = models.TextField(verbose_name="Beschreibung", blank=True, null=True, max_length=250)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Erstellt am")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Projekt", null=True, blank=True)


    def __str__(self):
        """
            Returns the name of the TestProcedure per default when calling the object
        """
        return self.name

"""
    Stores the result of a certain test procedure (:model:`user_tests.TestProcedure`) and creator (:model:`auth.User`)
"""
class TestProcedureResult(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Ersteller", null=True, blank=True)
    test_procedure = models.ForeignKey(TestProcedure, on_delete=models.CASCADE, verbose_name="Testprozedur", null=False, blank=False)

    created_at = models.DateTimeField(default=timezone.now, verbose_name="Erstellt am")


    def __str__(self):
        """
            Returns the name of the associated TestProcedure per default when calling the object
        """
        return self.test_procedure.name

"""
    Stores the result of a certain useracceptancetest (:model:`user_tests.UserAcceptanceTest`) and is assosciated to a procedure (:model:`user_tests.TestProcedureResult`)
"""
class UserAcceptanceTestResult(models.Model):
    test_procedure_result = models.ForeignKey(TestProcedureResult, on_delete=models.SET_NULL, verbose_name="Testprozedurresultat", null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now, verbose_name="Erstellt am")
    acceptance_test = models.ForeignKey(UserAcceptanceTest, on_delete=models.CASCADE, verbose_name="Akzeptanztest", null=False, blank=False)
    status = models.CharField(max_length=10, verbose_name="Test-Status",
                              choices=TestStatus.choices, default=TestStatus.PENDING)

    notes = models.TextField(verbose_name="Notizen", blank=True, null=True, max_length=300)


    def __str__(self):
        """
            Returns the name of the associated UserAcceptanceTest per default when calling the object
        """
        return f"Resultat zu Test {self.acceptance_test}"
