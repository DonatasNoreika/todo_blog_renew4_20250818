from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField


class Post(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = HTMLField()
    date_created = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='covers', null=True, blank=True)

    def comments_count(self):
        return self.comments.all().count()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']


class Comment(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(to="Post", on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.post} ({self.date_created})"