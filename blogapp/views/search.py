from django.shortcuts import render
from blogapp.models.Post import Post
from django.db.models import Q
from blogapp.models.Setting import Vul
from blogapp.models.Tag import Tags
def search(request):
    query=""
    result=[]
    if request.method=="GET":
        if request.GET['tagId']:
            query=request.GET.get("search", None)
            tagid=request.GET.get("tagId",None)
            result=Post.objects.filter(Q(title__icontains=query)|Q(content__icontains=query)&Q(tags=(Tags.objects.get(name=tagid).id)))
            xss = Vul.objects.filter(name="XSS").values()[0]['status']
            return render(request, 'blogapp/search.html', {'query':query, "result":result, "xss": xss})
        else:
            query=request.GET.get("search", None)
            result=Post.objects.filter(Q(title__icontains=query)|Q(content__icontains=query))
            xss = Vul.objects.filter(name="XSS").values()[0]['status']
            return render(request, 'blogapp/search.html', {'query':query, "result":result, "xss": xss})
