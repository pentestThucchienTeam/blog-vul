from django.http.request import HttpRequest
from blogapp.form import Vul
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import os
from decouple import config


# def setting (request):
#     VUL = config('VUL')
#     if request.method=="GET":
#         VUL = request.GET.get("XSS", "CSRF")
#         if VUL.is_valid():
#             return HttpResponse('Da luu')
#     return render(request, "blogapp/setting.html", {'VUL':VUL})

def setting(request):
    XSS=config('XSS')
    CSRF=config('CSRF')
    form = Vul()
    if request.method == 'POST':
        form = Vul(request.POST)
        if form.is_valid():
             form.save()
        return HttpResponseRedirect('/')
    return render(request,"blogapp/setting.html", {'form':form})