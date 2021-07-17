from django.db.models import query
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import jwt
from blogapp.models.Setting import Vul
from django.contrib.auth.decorators import login_required
from core.lib import jwt_vul
import base64
import json


@login_required
def setting (request):

    cookie_check = request.COOKIES['ten']
    
#     signature = cookie_check.split(".")[2]

#     header = cookie_check.split(".")[0]

#     if len(header) % 4 != 0:
#             header += '=' * (4 - len(header) % 4)

#     algorithm = json.loads(base64.urlsafe_b64decode(header).decode('utf-8'))
    jwt_confusion = Vul.objects.filter(name="JWT_Key_Confusion").values()[0]['status']
    if jwt_confusion:
        publickey = open("blogapp/views/pub.key","r").read()
        cookie_decode = jwt_vul.decode(cookie_check, publickey)
    else:
        import jwt
        publickey = open("blogapp/views/pub.key","r").read()
        cookie_decode=jwt.decode(cookie_check, publickey, algorithms=["RS256"])
        
    if not cookie_decode['admin']:
        return render(request, "blogapp/setting.html")
    
    print(request.session._session_key)
    ren = Vul.objects.all()
    query1=""
    query2=""
    query3=""
    query5=""
    xss=[]
    csrf=[]
    sqli=[]
    jwt_confusion=[]

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



    return render(request, "blogapp/setting.html",{'query1':query1,'query2':query2,'xss': xss, 'csrf':csrf,'ren':ren, 'sqli':sqli,'JWT_Key_Confusion':jwt_confusion})





