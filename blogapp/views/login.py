from  django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import LoginForm
from blogapp.models.Setting import Vul
from django.contrib.auth import authenticate, login
import time
from django.utils.http import http_date
import jwt


def create_cookie(user):
    jwts = Vul.objects.filter(name="JWT").values()[0]['status']
    if jwts:
        key = "anhyeuem"
    else:
        key = "pentestThucchienTeam"
    is_admin = user.is_superuser
    username = user.username
    payload = {"username": username, "admin": is_admin}
    return jwt.encode(payload, key, algorithm="HS256")


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
 
 
