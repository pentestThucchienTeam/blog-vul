from django.db import models
from django.db.models.deletion import CASCADE
from blogapp.models.User import user
# Create your models here.
class userprofile(models.Model):
    email = models.OneToOneField(user, on_delete=models.CASCADE, related_name='g_emails')
    username= models.OneToOneField(user, on_delete=models.CASCADE, related_name='g_usernames')
    phoneNumber = models.CharField(max_length=10, default='')
    firtName = models.CharField(max_length=10, default='')
    lastName = models.CharField(max_length=10, default='')
    avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank = True)
    status = models.BooleanField(default=True)
    facebook = models.CharField(max_length=200, default='', blank=True)
    github = models.CharField(max_length=200, default='', blank= True)
    twitter = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.lastName+''+self.firtName