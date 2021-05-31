from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models.Post import Post


def post(request, id):
    post_render = Post.objects.get(id= id)
    return render(request,'blogapp/post.html', {'post_render':post_render})