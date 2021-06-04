from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import messages

def setting(request):
    if request.method == 'GET':
        return render(request,"blogapp/setting.html",{})
    if request.method == 'POST':
       list = request.POST.getlist('vuls')
        
        mess = messages.add_message(request, messages.SUCCESS, 'Form submitted successfully.')
        return render(request, "blogapp/setting.html", {}) 
