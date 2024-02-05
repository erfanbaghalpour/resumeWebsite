from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.views.generic import ListView
from Comments.models import Comment, Reply
from Comments.forms import CommentForm, ReplyForm
from django.contrib import messages


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
    comment_form = CommentForm()
    detail_blog = get_object_or_404(Blog, id=blog_id, active=True)
    comments = detail_blog.comment_set.filter(active=True)
    reply_form = ReplyForm()
    # replies = detail_blog.reply_set.filter(active=True)
    replies = Reply.objects.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            name = comment_form.cleaned_data.get('name')
            email = comment_form.cleaned_data.get('email')
            text = comment_form.cleaned_data.get('text')
            Comment.objects.create(
                name=name,
                email=email,
                text=text,
                blog=detail_blog,
            )
            messages.add_message(request, messages.SUCCESS, 'Your comment has been successfully registered.')
            return redirect('Blog:blog_detail', detail_blog.id)
        messages.add_message(request, messages.ERROR, 'Your comment has not been successfully registered.')

    context = {
        'blog_detail': detail_blog,
        'comment_form': comment_form,
        'comments': comments,
        'replies': replies,
    }
    return render(request, 'Blog/Blog_Detail.html', context=context)
