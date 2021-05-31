from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models.Post import Post

def blog(request):
    object_list = Post.objects.all()
    return render(request, 'blogapp/blog.html', {'object_list': object_list})