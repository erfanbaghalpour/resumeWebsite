from django.urls import path, include
from .views import BlogList, BlogDetailView, add_blog_comment

app_name = 'Blog'
urlpatterns = [
    path('', BlogList.as_view(), name='blog_list'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('add-article-comment', add_blog_comment, name='add_blog_comment'),
]
