from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from Skills.models import Skill, Biography, Experience
from ContactUs.forms import ContactUsForm


# class Index(TemplateView):
#     template_name = 'core/index.html'

def index(request: HttpRequest):
    skills = Skill.objects.all()
    bio = Biography.objects.filter(is_active=True).first()
    experience = Experience.objects.all()
    contact_form = ContactUsForm()
    context = {
        'skills': skills,
        'bio': bio,
        'experience': experience,
        'form': contact_form,
    }
    return render(request, 'core/index.html', context=context)
