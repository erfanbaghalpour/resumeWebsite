from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from Skills.models import Skill, Biography, Experience


# class Index(TemplateView):
#     template_name = 'core/index.html'

def index(request: HttpRequest):
    skills = Skill.objects.all()
    bio = Biography.objects.filter(is_active=True).first()
    experience = Experience.objects.all()
    context = {
        'skills': skills,
        'bio': bio,
        'experience': experience,
    }
    return render(request, 'core/index.html', context=context)
