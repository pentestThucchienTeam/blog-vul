from  django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import LoginForm
from django.contrib.auth import authenticate, login

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
                try:
                    return redirect(request.GET['redirect_url'])
                except:
                    return redirect("/")
            
            else:
               msg = "Username, password meo dung"
        
        else:
            msg = "Co loi xay ra"
    return render(request, "blogapp/login.html", {"form": form, "msg": msg})
 
 
