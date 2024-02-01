from django.shortcuts import render, get_object_or_404
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
    paginate_by = 3
    context_object_name = 'blogs'


def blog_detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, id=blog_id, active=True)
    context = {
        'blog_detail': detail_blog
    }
    return render(request, 'Blog/Blog_Detail.html', context=context)
