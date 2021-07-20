from django.db.models import query
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .form import CommentForm
from blogapp.models.Post import Post
from blogapp.models.Tag import Tags
from blogapp.models.Comment import  Comment
from blogapp.models.Setting import Vul
class post:
    def post(request , id):
        object_list = Post.objects.all()
        listtag = Tags.objects.all()
        xss = Vul.objects.filter(name="XSS").values()[0]['status']
        sql = Vul.objects.filter(name="SQLI").values()[0]['status']
        if sql:
            post_render = Post.objects.raw("SELECT * FROM blogapp_post WHERE id = %s" % id) 
        else:
            post_render= get_object_or_404(Post,id=id)
        form = CommentForm()
        if request.method =="POST":
            form =CommentForm(data = request.POST,author_id=request.user, post_id=post_render, email=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.path)
        
        
        return render(request,'blogapp/post.html',{'object_list':object_list,'listtag':listtag,'post_render':post_render,'form':form,'xss':xss,'sql':sql})

