from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post, Comment
from django.contrib.auth.models import User

def index(request):
    context = {
        'num_posts': Post.objects.count(),
        'num_comments': Comment.objects.count(),
        'num_users': User.objects.count(),
    }
    return render(request, template_name="index.html", context=context)

