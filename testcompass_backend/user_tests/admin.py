from django.contrib import admin
from .models import UserAcceptanceTest, Project, UserAcceptanceTestResult, TestProcedure, TestProcedureResult

admin.site.register(Project)
admin.site.register(UserAcceptanceTest)
admin.site.register(UserAcceptanceTestResult)
admin.site.register(TestProcedure)
admin.site.register(TestProcedureResult)
