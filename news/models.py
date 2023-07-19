from django.db import models
from django.core.validators import MinValueValidator
from django.db import models
from datetime import datetime
from django.db.models import Sum
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subscribers = models.ManyToManyField(User, blank=True)

    def subscribe(self):
        pass    
    def get_category(self):
        return self.name
    def __str__(self):
        return f'{self.name.title()}'


class News(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField()
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news',
    )
    time_creation = models.DateTimeField(auto_now_add = True)
  
    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'
    
    def get_absolute_url(self):
        return f'/news/{self.id}'