from django.urls import path, include
from .views import BlogList, BlogDetailView

app_name = 'Blog'
urlpatterns = [
    path('', BlogList.as_view(), name='blog_list'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
]
