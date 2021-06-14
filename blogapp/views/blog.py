from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models.Post import Post
from blogapp.models.Setting import Vul

def blog(request):
    xss = Vul.objects.filter(name="XSS").values()[0]['status']
    object_list = Post.objects.all()
    return render(request, 'blogapp/blog.html', {'object_list': object_list, 'xss': xss})
