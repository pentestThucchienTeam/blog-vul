from django.db.models import query
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from blogapp.models.Setting import Vul
from django.contrib.auth.decorators import login_required
import base64
import json
import jwt
from decouple import config
from core.lib.jwt_vul.utils import base64url_decode, base64url_encode

class settingView(TemplateView):
    
    template_name = 'setting.html'
    jwts = Vul.objects.filter(name="JWT").values()[0]['status']
    jwt_confusion = Vul.objects.filter(name="JWT_Key_Confusion").values()[0]['status']


    def get(self, request):
        cookie_check = request.COOKIES['auth']

        if self.jwt_confusion and not self.jwts:

            ext, fake = cookie_check.split('.',1)
            header = base64url_decode(bytes(str(ext),'utf-8'))
            pubkey = json.loads(header.decode('utf-8'))    
            publickey = pubkey['publickey']

            from core.lib import jwt_vul
            cookie_decode = jwt_vul.decode(cookie_check, publickey)
            
        elif jwts:

            from core.lib import jwt_vul
            key = request.session['key']
            cookie_decode = jwt_vul.decode(cookie_check, key)

        else:
            
            key = request.session['key']
            cookie_decode = jwt.decode(cookie_check, key, algorithms="HS256")
        
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

        if not cookie_decode['admin']:
            block = 'staff'
            print()
            return render(request, "blogapp/setting.html",{'aut': 'staff', 'ren':ren, 'query1':query1,'query2':query2,'xss': xss, 'csrf':csrf, 'sqli':sqli,'JWT_Key_Confusion':jwt_confusion, 'jwt1':jwt1})
        return render(request, "blogapp/setting.html",{'aut': 'admin', 'ren':ren, 'query1':query1,'query2':query2,'xss': xss, 'csrf':csrf, 'sqli':sqli,'JWT_Key_Confusion':jwt_confusion, 'jwt1':jwt1})
        # else:    
        #     return render(request, "blogapp/setting.html",{'block': , 'ren':ren, 'query1':query1,'query2':query2,'xss': xss, 'csrf':csrf, 'sqli':sqli,'JWT_Key_Confusion':jwt_confusion, 'jwt1':jwt1})





