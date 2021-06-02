from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models.Post import Post
def post(request, id):
    post_render = Post.objects.get(id= id)
    object_list = Post.objects.all()
    '''if Post.objects.get(id=(id-1))!=None:
        post_previous =Post.objects.get(id=(id-1))
    if Post.objects.get(id=(id+1))!=None:
        post_next =Post.objects.get(id=(id+1))'''
    return render(request,'blogapp/post.html',
    {'post_render':post_render,'object_list':object_list})
    '''post_next':post_next,
    'post_previous':post_previous'''
    