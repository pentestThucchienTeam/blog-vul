from django.views.generic import TemplateView
from django.shortcuts import render

class requestpostView(TemplateView):
    template_name = "requestpost.html"
    def get(self, request):

        return render(request, self.template_name)
