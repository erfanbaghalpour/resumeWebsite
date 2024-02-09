from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.views.generic import ListView, DetailView
from Comments.models import Comment
from Comments.forms import CommentForm, CommentFormNew
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


# def blog_detail(request, blog_id):
#     comment_form = CommentForm()
#     detail_blog = get_object_or_404(Blog, id=blog_id, active=True)
#     comments = detail_blog.comment_set.filter(active=True)
#
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             name = comment_form.cleaned_data.get('name')
#             email = comment_form.cleaned_data.get('email')
#             text = comment_form.cleaned_data.get('text')
#             Comment.objects.create(
#                 name=name,
#                 email=email,
#                 text=text,
#                 blog=detail_blog,
#             )
#             messages.add_message(request, messages.SUCCESS, 'Your comment has been successfully registered.')
#             return redirect('Blog:blog_detail', detail_blog.id)
#         messages.add_message(request, messages.ERROR, 'Your comment has not been successfully registered.')
#
#     context = {
#         'blog_detail': detail_blog,
#         'comment_form': comment_form,
#         'comments': comments,
#     }
#     return render(request, 'Blog/Blog_Detail.html', context=context)

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'Blog/Blog_Detail.html'
    context_object_name = 'blog_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comment_set.filter(active=True, parent=None).prefetch_related(
            'comment_set')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            name = comment_form.cleaned_data.get('name')
            email = comment_form.cleaned_data.get('email')
            text = comment_form.cleaned_data.get('text')
            Comment.objects.create(
                name=name,
                email=email,
                text=text,
                blog=self.object,
            )
            messages.add_message(request, messages.SUCCESS, 'Your comment has been successfully registered.')
            return redirect('Blog:blog_detail', self.object.id)
        messages.add_message(request, messages.ERROR, 'Your comment has not been successfully registered.')
        context = self.get_context_data()
        context['comment_form'] = comment_form
        return self.render_to_response(context)
