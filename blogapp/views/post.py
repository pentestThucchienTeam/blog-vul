from django.db.models import query
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from .comment_form import CommentForm
from blogapp.models.Post import Post
from blogapp.models.Tag import Tags
from blogapp.models.Comment import  Comment
from blogapp.models.Setting import Vul

class postView(TemplateView):

    template_name = 'post.html'

    def get(self, request , id):
        form = CommentForm()
        postView.object_list = Post.objects.all()
        postView.listtag = Tags.objects.all()
        postView.xss = Vul.objects.filter(name="XSS").values()[0]['status']
        postView.sql = Vul.objects.filter(name="SQLI").values()[0]['status']
        if self.sql:
            postView.post_render = Post.objects.raw("SELECT * FROM blogapp_post WHERE id = %s" % id) 
        else:
            postView.post_render= get_object_or_404(Post,id=id)

        return render(request, self.template_name, {

            'object_list': self.object_list,
            'listtag': self.listtag, 
            'post_render': self.post_render, 
            'form': form,
            'xss': self.xss,
            'sql': self.sql
        })
    
    def post(self, request):    
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    
        return render(request, self.template_name, {

        'object_list': self.object_list,
        'listtag': self.listtag, 
        'post_render': self.post_render, 
        'form': form,
        'xss': self.xss, 
        'sql': self.sql
    })    

