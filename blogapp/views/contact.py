from django.views.generic.list import View
from django.shortcuts import render

class contact(View):
    template_name = "contact.html"
    def get(self,request):
        return render(request,self.template_name)