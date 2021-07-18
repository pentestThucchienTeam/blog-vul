from django.db.models import query
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blogapp.models.Setting import Vul
from django.contrib.auth.decorators import login_required
import base64
import json
import jwt


@login_required(login_url="/login")
def setting (request):

    jwts = Vul.objects.filter(name="JWT").values()[0]['status']
    jwt_confusion = Vul.objects.filter(name="JWT_Key_Confusion").values()[0]['status']
    cookie_check = request.COOKIES['ten']

    if jwt_confusion and not jwts:
        from core.lib import jwt_vul
        with open("blogapp/views/pub.key","r") as filekey:
            publickey= filekey.read()
        cookie_decode = jwt_vul.decode(cookie_check, publickey)
        
    elif jwts:
        from core.lib import jwt_vul
        key = request.session['key']
        cookie_decode = jwt_vul.decode(cookie_check, key)               
    else:
        key = request.session['key']
        cookie_decode = jwt.decode(cookie_check, key, algorithms="HS256")

    if not cookie_decode['admin']:
        return render(request, "blogapp/setting.html")
    
    ren = Vul.objects.all()
    query1 = query2 = query3 = query4 = query5 = ""
    xss = csrf = sqli = jwt1 = jwt_confusion = ""
  
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
        query5 = request.POST.get('JWT_Key_Confusion',None)
        if query5=="1":
                jwt_confusion = Vul.objects.filter(name="JWT_Key_Confusion").update(status="True")
        else:
            jwt_confusion = Vul.objects.filter(name="JWT_Key_Confusion").update(status="False")

        query4 = request.POST.get('JWT',None)
        if query4=="1":
                jwt1 = Vul.objects.filter(name="JWT").update(status="True")
        else:
            jwt1 = Vul.objects.filter(name="JWT").update(status="False")

    return render(request, "blogapp/setting.html",{'query1':query1,'query2':query2,'xss': xss, 'csrf':csrf,'ren':ren, 'sqli':sqli,'JWT_Key_Confusion':jwt_confusion, 'jwt1':jwt1})





