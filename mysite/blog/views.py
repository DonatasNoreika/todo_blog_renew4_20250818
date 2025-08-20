from django.shortcuts import render, reverse
from .models import Post, Comment, CustomUser
from django.contrib.auth.models import User
from django.views import generic
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from .forms import CommentForm, CustomUserChangeForm, CustomUserCreateForm


def index(request):
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_posts': Post.objects.count(),
        'num_comments': Comment.objects.count(),
        'num_users': CustomUser.objects.count(),
        'num_visits': num_visits,
    }
    return render(request, template_name="index.html", context=context)


def search(request):
    query = request.GET.get('query')
    context = {
        "query": query,
        "posts": Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(author__username__icontains=query)),
    }
    return render(request, template_name="search.html", context=context)


class SignUpView(generic.CreateView):
    form_class = CustomUserCreateForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')
    context_object_name = "user"

    def get_object(self, queryset=None):
        return self.request.user


class PostListView(generic.ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "posts"
    paginate_by = 5


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"
    form_class = CommentForm

    def get_success_url(self):
        return reverse("post", kwargs={"pk": self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.post = self.get_object()
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class UserPostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'user_posts.html'
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
