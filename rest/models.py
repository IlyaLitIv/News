from ipaddress import summarize_address_range
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.

class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    raitingAuthor = models.SmallIntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.all().aggregate(postRating=summarize_address_range('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.all().aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.raitingAuthor = pRat * 3 + cRat
        self.save()


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
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.commentUser.username
        # return self.commentPost.author.authorUser.username

    def like(self):
        self.rating += 1
        self.save()

    def deslike(self):
        self.rating -= 1
        self.save()