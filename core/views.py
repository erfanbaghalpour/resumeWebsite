from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from Skills.models import Skill, Biography, Experience
from ContactUs.forms import ContactUsForm
from ContactUs.models import ContactUs
from django.contrib import messages


# class Index(TemplateView):
#     template_name = 'core/index.html'

def index(request: HttpRequest):
    skills = Skill.objects.all()
    bio = Biography.objects.filter(is_active=True).first()
    experience = Experience.objects.all()
    if request.method == "POST":
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data.get("name")
            email = contact_form.cleaned_data.get("email")
            subject = contact_form.cleaned_data.get("subject")
            text = contact_form.cleaned_data.get("text")
            # ContactUs.objects.create(
            #     name=name,
            #     email=email,
            #     subject=subject,
            #     text=text,
            # )
            new_contact = ContactUs(
                name=name,
                email=email,
                subject=subject,
                text=text,
            )
            new_contact.save()
            messages.add_message(request, messages.SUCCESS, 'Your message has been successfully received!')
            return redirect("core:index")
        else:
            messages.add_message(request, messages.ERROR,
                                 'Your message has not been registered. Please fix the existing errors!')
    else:
        contact_form = ContactUsForm()
    context = {
        'skills': skills,
        'bio': bio,
        'experience': experience,
        'form': contact_form,
    }
    return render(request, 'core/index.html', context=context)

# def index(request: HttpRequest):
#     skills = Skill.objects.all()
#     bio = Biography.objects.filter(is_active=True).first()
#     experience = Experience.objects.all()
#
#     if request.method == "POST":
#         contact_form = ContactUsForm(request.POST)
#
#         if contact_form.is_valid():
#             name = contact_form.cleaned_data.get("name")
#             email = contact_form.cleaned_data.get("email")
#             subject = contact_form.cleaned_data.get("subject")
#             text = contact_form.cleaned_data.get("text")
#
#             ContactUs.objects.create(
#                 name=name,
#                 email=email,
#                 subject=subject,
#                 text=text,
#             )
#
#             return redirect("core:index")
#     else:
#         contact_form = ContactUsForm()
#
#     context = {
#         'skills': skills,
#         'bio': bio,
#         'experience': experience,
#         'form': contact_form,
#     }
#
#     return render(request, 'core/index.html', context=context)
