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
    privatekey= b"-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEApwOkzVqmWqFGfdPUSU73A3UqwlqRdA40pDhyuIN56yZWRXVqp8Hgxl3ai5gFayhbJAkg1Z5wUKFVFmCa7J6j97QAzTDNHA17YPOu/WoRBuQobSL8A1epiBpnRfQn/+gabWYG4jRBZ6q0Zjh12qAJvdO6Fq+e0sfp7gvgp5XXJhqIGiOCTT5hDHFygefjmSA9TX3xOSrlPMUrnDzrhfgapIEMlx6xli3hhEfCo0ISCMI4S/r+35GHayezbtdz7mLOF8ODuagEX0HDyoLvJ5q14NrCLStIY1plWUDJ3DVFKjMbSREVTzRSmU1sMrgEztG+hG23iUNGwo4zH53U4sHduwIDAQABAoIBACJH8S/lh3fa2qlBLbXOa41eI2S5SlnUAKIkpAeTlRbbS6H+M+IzPXv6D73Pem1AX1TKOt8eIleqhdiOA77F4UoavH9hoPg9HDIOUsDZYJ1Vf6bHI4tcFwRExyXos70nWyVRZ+BOcY5hz52bwTUa3GUGbI/zhFonhrDB517+tqavPoLpdR5JlK8kXcf2DPEQnnmak7xR958BPukezXZKPjUhZS8gz6Q5LIc6m79Rehj7DvQStrQtTIVqlGRH++5e8WStGXZFPsot57UEuraDj9UYvoQ8G4DI98ukiaINcM7GBKVDMcjdcientFuHW339D/DWYkP+//8IHAIKWMiSkyECgYEA15PVsWaGvmr/3oZkDrvd1k5OQajOJ4Ou30Cuess4B0zTDOORvzpo4N36Kc5lwIngpnzuC4LSidHMNcA7mEKT8/DHY36uAw3Cf8SqyhScL14rx3yb6SA9/jovSMZOJNP5iVgqzj1i0GsNIIUC837N7J6MSBnkZcitc1sxYtikTNUCgYEAxlSsNRVUPSVEknQsHwZCfLm+FeS/7grTgJvY6ka+xaIikxCIyIwq/g3FIPpdn6Bt3Va+y8y44zWAc7tQaqkWytvhcTyZiaoqqF9upOX2aWtNjMAKAq4hVvjFvPHWoSHMf2F83bcE1XAPzirIMWkf8tKnS3W9pseik0VUkLzJiE8CgYEA0aPeR6oglsSPFuMyInHnhSSZTZjPAfY49Lp98sP1NIQtKXeUoJY4r5SuVkF1CgwK/1y2UVNjUstG/251hdgY8TzRaZwjtKyI3J9wRxxL1nSJtnEjXU4Re00x9l+CVqYdIMcwuWdQ1MWF+n3fJNPHhbeZS/SB+8lvg6LHIAz1mhECgYEAvgCmTeCWKFIIxImZL0uu7JCBg7X3DZS/lQk5IRAPeYTfvKZtdDucgHEutm5EvUVTm2WcOeByC/HYkocT/mrpVASckQAuU417enyaok1Q6SOMUtgzfufVNt3zihThutKHeE0r87h/X/8QlUG1Mmj024tmDEvLGflNTetwnYzPQc8CgYARdMvpqDbnTG79I8JI41Bn8JNVcBj+++erN5sNYXLJBegy+PVZnivDGoxRVE1ne20ZpU8ao0OGHdyXkWj3cJUAczjdekvIzu1k8OdUIBtcNz1J1pvIR/V/wiWwQZtpSaCO6WrOrvyrKf9ZzkrVWMfde9biCwNlZMCnwS6/HUaH0A==\n-----END RSA PRIVATE KEY-----"

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
 
 
