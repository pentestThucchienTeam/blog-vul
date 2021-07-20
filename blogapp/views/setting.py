from django.views.generic import ListView
from blogapp.models.Setting import Vul
from django.shortcuts import render

class settingView(ListView):
	
	template_name = 'setting.html'
	model = Vul
