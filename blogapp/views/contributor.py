from django.views.generic.list import View
from django.shortcuts import render

class contributorView(View):
    template_name = "contributor.html"
    def get(self,request):
        return render(request,self.template_name)