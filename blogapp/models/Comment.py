from django.db import models
from blogapp.models.Post import Post
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    Post_id = models.ManyToManyField(Post)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_id')
    content = models.TextField(default='')
    status = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='email_id')
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True )
    
    

    def __str__(self):
        return self.content 