from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'blogapp/index.html', {})
def post(request):
    return render(request, 'blogapp/post.html', {})
def blog(request):
    return render(request, 'blogapp/blog.html', {})
