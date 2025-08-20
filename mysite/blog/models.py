from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import AbstractUser
from PIL import Image

class Post(models.Model):
    author = models.ForeignKey(to="blog.CustomUser", on_delete=models.CASCADE)
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
    author = models.ForeignKey(to="blog.CustomUser", on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.post} ({self.date_created})"


class CustomUser(AbstractUser):
    photo = models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        min_side = min(img.width, img.height)
        left = (img.width - min_side) // 2
        top = (img.height - min_side) // 2
        right = left + min_side
        bottom = top + min_side
        img = img.crop((left, top, right, bottom))
        img = img.resize((300, 300), Image.LANCZOS)
        img.save(self.photo.path)