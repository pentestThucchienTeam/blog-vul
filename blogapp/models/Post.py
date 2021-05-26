from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from blogapp.models.Tag import  Tags
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=30, default='')
    tags = models.ManyToManyField(Tags)
    status = models.CharField(max_length=50, default='')
    content = RichTextField(default='')
    creat_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author_id = models.ManyToManyField(User)
    images = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True )
    
    def __str__(self):
        return f'{self.title}'



