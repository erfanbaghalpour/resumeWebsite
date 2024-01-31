from django.urls import path, include
from .views import BlogList, blog_detail

app_name = 'Blog'
urlpatterns = [
    path('', BlogList.as_view(), name='blog_list'),
    path('detail/<int:blog_id>', blog_detail, name='blog_detail'),
]
