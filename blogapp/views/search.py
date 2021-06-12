  
from django import db
from django.http.response import HttpResponse
from django.shortcuts import render
from blogapp.models.Post import Post
from django.db.models import Q
from django.template.loader import render_to_string
from blogapp.models.Setting import Vul
from django.db import connection
def search(request):
    query=""
    result=[]
    xss = Vul.objects.filter(name="XSS").values()[0]['status']
    sql = Vul.objects.filter(name="SQLI").values()[0]['status']
    if request.method=="GET":
        query=request.GET.get("search", None)
        if sql:
          sqli=   "SELECT * FROM blogapp_post WHERE title ILIKE '%s'"%query
          result=Post.objects.raw(sqli)
        else:
          result=Post.objects.filter(Q(title__icontains=query)|Q(content__icontains=query))


    html = render_to_string('blogapp/search.html',
    {'query':query, "result":result, "xss": xss, 'sql':sql})

    return HttpResponse(html)