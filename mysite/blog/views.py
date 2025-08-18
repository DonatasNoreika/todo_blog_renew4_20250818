from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post, Comment
from django.contrib.auth.models import User
from django.views import generic
from django.db.models import Q

def index(request):
    context = {
        'num_posts': Post.objects.count(),
        'num_comments': Comment.objects.count(),
        'num_users': User.objects.count(),
    }
    return render(request, template_name="index.html", context=context)

def search(request):
    query = request.GET.get('query')
    context = {
        "query": query,
        "posts": Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(author__username__icontains=query) )
    }
    return render(request, template_name="search.html", context=context)

class PostListView(generic.ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "posts"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"
