from django.urls import path
from .views import index
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', index, name="index"),
    path('posts/', PostListView.as_view(), name="posts"),
    path('posts/<int:pk>', PostDetailView.as_view(), name="post"),
]