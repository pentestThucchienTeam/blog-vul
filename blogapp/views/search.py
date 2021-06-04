from django.shortcuts import render
from blogapp.models.Post import Post
from django.db.models import Q
from blogapp.models.Vul import Vul
def search(request):
    query=""
    result=[]
    if request.method=="GET":
        query=request.GET.get("search", None)
        result=Post.objects.filter(Q(title__icontains=query)|Q(content__icontains=query))
        print(type(result))
        xss = Vul.objects.filter(name="XSS").values()[0]['status']
        print(type(xss))
        return render(request, 'blogapp/search.html', {'query':query, "result":result, "xss": xss})
