from django.http.response import HttpResponse
from blogapp.forms import RegistrationForm
from django.http import HttpResponseRedirect 
from django.http import HttpResponse
from django.shortcuts import render

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog')
    return render(request, 'blogapp/register.html', {'form': form})


