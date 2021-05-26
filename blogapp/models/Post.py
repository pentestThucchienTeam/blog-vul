from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BigAutoField, CharField
from blogapp.models.Tag import Catalogies, Tags
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50, default='')
    tags = models.ManyToManyField(Tags)
    catalogies = models.OneToOneField(Catalogies, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    content = models.TextField(default='')
    creat_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    images = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True )
    author_id = models.ManyToManyField(User)
    
    def __str__(self):
        return f'{self.title}'



