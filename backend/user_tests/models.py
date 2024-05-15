from django.db import models
from organizations.models import Organization
from django.utils import timezone
from django.contrib.auth.models import User

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
        return self.name

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
        return self.name

class TestProcedure(models.Model):
    acceptance_tests = models.ManyToManyField(UserAcceptanceTest, null=True, blank=True)
    name = models.CharField(max_length=150, blank=False, null=False, verbose_name="Name")
    description = models.TextField(verbose_name="Beschreibung", blank=True, null=True, max_length=250)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Erstellt am")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Projekt", null=True, blank=True)


    def __str__(self):
        return self.name

class TestProcedureResult(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Ersteller", null=True, blank=True)
    test_procedure = models.ForeignKey(TestProcedure, on_delete=models.CASCADE, verbose_name="Testprozedur", null=False, blank=False)

    created_at = models.DateTimeField(default=timezone.now, verbose_name="Erstellt am")


    def __str__(self):
        return self.test_procedure.name

class UserAcceptanceTestResult(models.Model):
    test_procedure_result = models.ForeignKey(TestProcedureResult, on_delete=models.CASCADE, verbose_name="Testprozedurresultat", null=False, blank=False)

    created_at = models.DateTimeField(default=timezone.now, verbose_name="Erstellt am")
    acceptance_test = models.ForeignKey(UserAcceptanceTest, on_delete=models.CASCADE, verbose_name="Akzeptanztest", null=False, blank=False)


    def __str__(self):
        return f"Resultat zu Test {self.acceptance_test}"
