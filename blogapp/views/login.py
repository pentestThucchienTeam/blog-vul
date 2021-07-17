from  django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import LoginForm
from django.contrib.auth import authenticate, login
import time
from django.utils.http import http_date
from core.lib import jwt_vul


def create_cookie(user):
    is_admin = user.is_superuser
    username = user.username
    payload = {"username": username, "admin": is_admin}    
    privatekey= open("home/kali/blog/blog-vul/blogapp/views/priv.pem","r").read()
    return jwt_vul.encode(payload, privatekey, algorithm="RS256").decode()


def login_view(request):
    form = LoginForm(request.POST or None)
    
    msg = None
    
    if request.method == "POST":
        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request,user)
                cookie_name = create_cookie(user)
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
 
 
