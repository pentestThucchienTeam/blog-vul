from blogapp.models.Tag import Tags
from django import db
from django.http.response import HttpResponse
from django.shortcuts import render
from blogapp.models.Post import Post

class tag:
    def tags (request, tag):

        tag_post = Post.objects.filter(tags__name=tag)

        return render(request, 'blogapp/tags.html',{'tag':tag,'tag_post':tag_post})
