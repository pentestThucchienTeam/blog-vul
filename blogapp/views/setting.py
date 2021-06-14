from django.db.models import query
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blogapp.models.Setting import Vul



def setting (request):
    ren = Vul.objects.all()
    query1=""
    query2=""
    query3=""
    xss=[]
    csrf=[]
    sql=[]


    if request.method =="POST":
        query1 = request.POST.get('XSS',None)
        if query1 == "1":
                xss=Vul.objects.filter(name="XSS").update(status=True)
        else :
                xss=Vul.objects.filter(name='XSS').update(status=False)


        query2 = request.POST.get('CSRF',None)
        if query2=="1":
                csrf = Vul.objects.filter(name="CSRF").update(status="True")
        else:
            csrf = Vul.objects.filter(name="CSRF").update(status="False")
        query3 = request.POST.get('SQLI',None)
        if query3=="1":
                sqli = Vul.objects.filter(name="SQLI").update(status="True")
        else:
            sqli = Vul.objects.filter(name="SQLI").update(status="False")



    return render(request, "blogapp/setting.html",{'query1':query1,'query2':query2,'xss': xss, 'csrf':csrf,'ren':ren, 'sql':sql})





