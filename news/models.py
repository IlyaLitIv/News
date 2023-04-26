from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

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
 
 

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
 
    def __str__(self):
        return f'{self.name.title()}'