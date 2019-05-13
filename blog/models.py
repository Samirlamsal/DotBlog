from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField( default='deafult.jpg',upload_to='profile_pic')
    Bio = models.TextField()

    def __str__(self):
        return f'{self.username} Profile'