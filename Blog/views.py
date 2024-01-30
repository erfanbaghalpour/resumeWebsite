from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView


# def blog_list(request):
#     blogs = Blog.objects.filter(active=True)
#     context = {
#         'blogs': blogs
#     }
#     return render(request, 'Blog/Blog.html', context=context)

class BlogList(ListView):
    # model = Blog
    queryset = Blog.objects.filter(active=True)
    template_name = "Blog/Blog.html"
    paginate_by = 1
    context_object_name = 'blogs'
