from core.lib.jwt_vul.get_key import get_key 
from  django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import LoginForm
from blogapp.models.Setting import Vul
from django.contrib.auth import authenticate, login
import time
from django.utils.http import http_date
import jwt
import json
from decouple import config
from blogapp.models.Setting import Vul

def create_cookie(user, request):
    jwt_confusion = Vul.objects.filter(name="JWT_Key_Confusion").values()[0]['status']
    jwts = Vul.objects.filter(name="JWT").values()[0]['status']

    is_admin = user.is_superuser
    username = user.username
    payload = {"username": username, "admin": is_admin}

    if jwt_confusion and not jwts:
        from core.lib import jwt_vul    
        with open(config('PRIVATEKEY'),"r") as filekey:
            privatekey=filekey.read()
        with open(config('PUBLICKEY'),"r") as pubkey:
            embedded=pubkey.read()
        return jwt_vul.encode(payload, privatekey, algorithm="RS256",headers={"publickey":embedded}).decode()
    
    elif jwts:
        from core.lib import jwt_vul
        key = get_key.weak()
        request.session['key'] = key
        return jwt_vul.encode(payload, key, algorithm="HS256").decode()
    else:
        key = get_key.secrure()
        request.session['key'] = key
        return jwt.encode(payload, key, algorithm="HS256")


def login_view(request):
    form = LoginForm(request.POST or None)
    
    msg = None
    
    if request.method == "POST":
        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()
            user = authenticate(username=username, password=password)
            # print(vars(request.session))
            
            if user is not None:
                login(request,user)

                cookie_name = create_cookie(user, request)
                try:
                    max_age = request.session.get_expiry_age()
                    expires_time = time.time() + max_age
                    expires = http_date(expires_time)
                    response = redirect(request.GET['next'])
                    response.set_cookie(
                        'ten',cookie_name,
                        max_age=max_age, expires=expires)
                    return response
                except:
                    max_age = request.session.get_expiry_age()
                    expires_time = time.time() + max_age
                    expires = http_date(expires_time)
                    response = redirect("/")
                    response.set_cookie(
                        'ten',cookie_name,
                        max_age=max_age, expires=expires)
                    return response
            
            else:
               msg = "Username, password meo dung"
        
        else:
            msg = "Co loi xay ra"
    return render(request, "blogapp/login.html", {"form": form, "msg": msg})
 
 
