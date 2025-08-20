from django.urls import path
from .views import index, search
from .views import (PostListView,
                    PostDetailView,
                    UserPostListView,
                    SignUpView,
                    ProfileUpdateView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    CommentUpdateView,
                    CommentDeleteView)

urlpatterns = [
    path('', index, name="index"),
    path('search', search, name="search"),
    path('posts/', PostListView.as_view(), name="posts"),
    path('posts/<int:pk>', PostDetailView.as_view(), name="post"),
    path('userposts/', UserPostListView.as_view(), name="userposts"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path("posts/new", PostCreateView.as_view(), name="post_new"),
    path("posts/<int:pk>/update", PostUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),
    path("comments/<int:pk>/update", CommentUpdateView.as_view(), name="comment_edit"),
    path("comments/<int:pk>/delete", CommentDeleteView.as_view(), name="comment_delete"),
]