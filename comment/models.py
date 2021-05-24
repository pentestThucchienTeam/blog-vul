from django.db import models
from post.models import Post
from guser.models import guestuser

# Create your models here.
class Comment(models.Model):
    Post_id = models.ManyToManyField(Post)
    author_id = models.ForeignKey(guestuser, on_delete=models.CASCADE,related_name='user_id')
    content = models.TextField(default='')
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True )
    status = models.BooleanField(default=False)
    creaaTime = models.DateTimeField(auto_now_add=True)
    email = models.OneToOneField(guestuser, on_delete=models.CASCADE, related_name='emails')

    def __str__(self):
        return self.content, self.author_id