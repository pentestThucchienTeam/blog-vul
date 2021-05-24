from django.db import models
from django.db.models.fields import BigAutoField, CharField
from blogapp.models.Tag import Tags
from blogapp.models.User import User

class Post(models.Model):

    title = models.CharField(max_length=50, default='')
    tags = models.ManyToManyField(Tags)
    status = models.BooleanField(default=False)
    content = models.TextField(default='')
    creat_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    images = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True )
    author_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='authors_id')
    
    def __str__(self):
        return self.title, self.author_id