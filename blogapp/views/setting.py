from django.db.models import query
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blogapp.models.Setting import Vul



def setting (request):

    query1=""
    query2=""
    xss=[]
    csrf=[]

    if request.method =="POST":
        query1 = request.POST.get('XSS',None)
        if query1 == "1":
                xss=Vul.objects.filter(name="XSS").update(status="True")
        else :
                xss=Vul.objects.filter(name='XSS').update(status="False")


        query2 = request.POST.get('CSRF',None)
        if query2=="1":
                csrf = Vul.objects.filter(name="CSRF").update(status="True")
        else:
            csrf = Vul.objects.filter(name="CSRF").update(status="False")

        return HttpResponseRedirect('/')

    return render(request, "blogapp/setting.html",{'query1':query1,'query2':query2,'xss': xss, 'csrf':csrf})
