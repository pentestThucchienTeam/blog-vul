from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models.Post import Post
from blogapp.models.Setting import Vul


def post(request, id):
    xss = Vul.objects.filter(name="XSS").values()[0]['status']
    post_render = Post.objects.get(id= id)
    object_list = Post.objects.all()
    return render(request,'blogapp/post.html',
    {'post_render':post_render,'object_list':object_list, 'xss': xss})
    
