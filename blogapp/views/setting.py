from django.db.models import query
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blogapp.models.Setting import Vul
from django.contrib.auth.decorators import login_required
import jwt


@login_required
def setting (request):

    cookie_check = request.COOKIES['ten']

    cookie_decode = jwt.decode(cookie_check, "secret", algorithms="HS256")

    if not cookie_decode['admin']:
        return render(request, "blogapp/setting.html")
    
    print(request.session._session_key)
    ren = Vul.objects.all()
    query1=""
    query2=""
    query3=""
    xss=[]
    csrf=[]
    sqli=[]

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



    return render(request, "blogapp/setting.html",{'query1':query1,'query2':query2,'xss': xss, 'csrf':csrf,'ren':ren, 'sqli':sqli})





