from blogapp.models.Tag import Tags
from django.views.generic.base import TemplateView
from django import db
from django.http.response import HttpResponse
from django.shortcuts import render
from blogapp.models.Post import Post

class tags(TemplateView):
    template_name = 'blogapp/tags.html'

    def tags (self,request, tag):

        tag_post = Post.objects.filter(tags__name=tag)
        args = {'tag':tag,'tag_post':tag_post}
        return render(request, self.template_name, args)
