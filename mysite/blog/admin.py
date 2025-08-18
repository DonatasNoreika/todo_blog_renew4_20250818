from django.contrib import admin
from .models import Post, Comment

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'date_created']

class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'date_created', 'author', 'comments_count']
    list_filter = ['author']
    list_editable = ['title', 'author']
    search_fields = ['title', 'content']
    inlines = [CommentInLine]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
