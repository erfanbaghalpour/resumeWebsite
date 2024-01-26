from django.http import HttpRequest
from django.shortcuts import render

from .models import Setting, SocialMedia


# def setting_processor(request: HttpRequest):
#     setting = Setting.objects.first()
#     social_media_list = SocialMedia.objects.first()
#     context = {
#         'setting': setting,
#         'social_media_list': social_media_list
#     }
#     return context
def setting_processor(request):
    setting = Setting.objects.first()
    social_media_list = SocialMedia.objects.all()
    context = {
        'setting': setting,
        'social_media_list': social_media_list,
    }
    return context
    # return render(request, '', context)
