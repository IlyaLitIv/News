from django.contrib import admin
from .models import Category, News
from rest.models import Author, Post, PostCategory, Comment
# Author, Post, PostCategory, Comment

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(News)

  
