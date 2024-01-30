from django.urls import path, include
from .views import BlogList

app_name = 'Blog'
urlpatterns = [
    path('', BlogList.as_view(), name='blog_list')
]
