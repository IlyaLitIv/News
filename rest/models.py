from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    raiting = models.IntegerField()
    def update_raiting(self):
        self.raiting = self.raiting*3 
        self.save()    
    author = models.OneToOneField(User, on_delete = models.CASCADE)


class Category(models.Model):
    category_name = models.CharField(max_length = 255, unique = True)
    

class Post(models.Model):
    news = 'NW'
    article = "AR"
    POSITIONS = [
        ('NW',"новости"),('AR',"статья")]
    field = models.CharField(max_length = 10,
                             choices = POSITIONS, 
                             default = news)
    time_creation = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 30, default = "Заголовок")
    body = models.TextField(default = "Содержание")
    raiting = models.IntegerField()
    def like(self):
        self.raiting += 1
        self.save()   
    def dislike(self):
        self.raiting -= 1
        self.save() 
    def preview(self):
        return self.body[0:255] + '...'

    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    category = models.ManyToManyField(Category, through = 'PostCategory')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField(default = "Содержание")
    time_creation = models.DateTimeField(auto_now_add = True)
    raiting = models.IntegerField()
    def like(self):
        self.raiting += 1
        self.save()   
    def dislike(self):
        self.raiting -= 1
        self.save()  