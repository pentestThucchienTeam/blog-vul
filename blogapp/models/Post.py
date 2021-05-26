from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BigAutoField, CharField
from blogapp.models.Tag import Catalogies, Tags
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50, default='')
    tags = models.ManyToManyField(Tags, through='Post_tags')
    catalogies = models.ManyToManyField(Catalogies, through='Post_cat')
    status = models.BooleanField(default=False)
    content = models.TextField(default='')
    creat_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    images = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True )
    author_id = models.ManyToManyField(User, through='Author')
    
    def __str__(self):
        return self.title

class Author(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Post_tags(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)

class Post_cat(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    cat = models.ForeignKey(Catalogies, on_delete=models.CASCADE)

