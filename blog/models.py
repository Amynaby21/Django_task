from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    Author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()
    
    class Meta:
        verbose_name_plural = 'Post'