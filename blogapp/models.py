from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=6)
    username = models.CharField(max_length=6, primary_key=True)
    password = models.CharField(max_length=15, )
    email = models.EmailField(max_length=254)


class Tag(models.Model):
    id = models.CharField(max_length=6)
    name = models.CharField(max_length=20)
    tags = models.CharField(max_length=20, primary_key=True)


class Profile(models.Model):
    id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    phoneNumber = models.CharField(max_length=10)
    firtName = models.CharField(max_length=7)
    lastName = models.CharField(max_length=7)
    avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    status = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)


class Post(models.Model):   
    id = models.CharField(max_length=6, primary_key=True)
    title = models.CharField(max_length=30)
    tags = models.OneToOneField(Tag, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    content = models.TextField
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now_add=True)
    authorid = models.OneToOneField(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)


class Comment(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    content = models.TextField
    status = models.BooleanField
    creaaTime = models.DateTimeField(auto_now_add=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    url = models.URLField
    email = models.OneToOneField(Profile, on_delete=models.CASCADE)
    post_id = models.OneToOneField(Post, on_delete=models.CASCADE)
