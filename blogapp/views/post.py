from django.shortcuts import render
from django.http import HttpResponse


def post(request):
    return render(request, 'blogapp/post.html', {})

