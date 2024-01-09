from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'core/index.html'
