from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .form import CommentForm
from blogapp.models.Post import Post
from blogapp.models.Comment import  Comment
from blogapp.models.Setting import Vul
def posto(request):
    object_list = Post.objects.all()
    xss = Vul.objects.filter(name="XSS").values()[0]['status']
    
    
    return render(request,'blogapp/post.html',{'object_list':object_list, 'xss':xss})
    '''post_next':post_next,
    'post_previous':post_previous'''
    
