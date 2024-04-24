from django.shortcuts import render
from django.views import View
from django.views.generic import FormView, ListView, TemplateView, CreateView, DetailView
from django.http import JsonResponse, HttpResponse,Http404
from .models import UserAcceptanceTest
class TestView(View):
    def get(self, request, *args, **kwargs):
        tests = UserAcceptanceTest.objects.filter(creator=self.request.user)


        test_list = list(tests.values())

        return JsonResponse(test_list, safe=False)
