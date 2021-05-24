from django.shortcuts import render
from django.http import HttpResponse

def blog(request):
    return render(request, 'blogapp/blog.html', {})