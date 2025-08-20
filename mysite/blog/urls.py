from django.urls import path
from .views import index, search
from .views import (PostListView,
                    PostDetailView,
                    UserPostListView,
                    SignUpView,
                    ProfileUpdateView)

urlpatterns = [
    path('', index, name="index"),
    path('search', search, name="search"),
    path('posts/', PostListView.as_view(), name="posts"),
    path('posts/<int:pk>', PostDetailView.as_view(), name="post"),
    path('userposts/', UserPostListView.as_view(), name="userposts"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
]