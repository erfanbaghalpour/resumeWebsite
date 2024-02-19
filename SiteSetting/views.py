from django.shortcuts import render
from django.views.generic.base import TemplateView


class RobotsTxtView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'
