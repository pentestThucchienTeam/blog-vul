from django.shortcuts import render
from blogapp.models.Post import Post
from django.db.models import Q


def search(request):
    query=""
    result=[]
    if request.method=="POST":
        query=request.POST.get("search", None)
        result=Post.objects.filter(Q(title__icontains=query)|Q(content__icontains=query))
    return render(request, 'blogapp/search.html', {'query':query, "result":result})