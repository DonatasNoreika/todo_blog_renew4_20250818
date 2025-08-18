from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post, Comment
from django.contrib.auth.models import User
from django.views import generic


def index(request):
    context = {
        'num_posts': Post.objects.count(),
        'num_comments': Comment.objects.count(),
        'num_users': User.objects.count(),
    }
    return render(request, template_name="index.html", context=context)


class PostListView(generic.ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "posts"


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"
