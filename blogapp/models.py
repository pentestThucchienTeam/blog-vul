from django.db import models

class User(models.Model):
    username = models.CharField(max_length=6, default='')
    password = models.CharField(max_length=15, default='')
    email = models.EmailField(max_length=254, default='')


class Tags(models.Model):
    name = models.CharField(max_length=20, default='')
    tags = models.CharField(max_length=20, default='')

class Profile(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    phoneNumber = models.CharField(max_length=10, default='')
    firtName = models.CharField(max_length=7, default='')
    lastName = models.CharField(max_length=7, default='')
    avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    status = models.TextField(default='')
    facebook = models.CharField(max_length=200, default='')
    github = models.CharField(max_length=200, default='')
    twitter = models.CharField(max_length=200, default='')


class Post(models.Model):   
    title = models.CharField(max_length=30, default='')
    tags = models.OneToOneField(Tags, on_delete=models.CASCADE, default='')
    status = models.TextField(default='')
    content = models.TextField(default='')
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now_add=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    images = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)


class Comment(models.Model):
    content = models.TextField(default='')
    status = models.TextField(default='')
    creaaTime = models.DateTimeField(auto_now_add=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE, default='', related_name='cmt_user')
    url = models.URLField
    email = models.OneToOneField(User, on_delete=models.CASCADE,default='', related_name='cmt_email')

