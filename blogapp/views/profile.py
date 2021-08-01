from blogapp.models.Userprofile import Userprofile as profile
from django.views.generic import TemplateView
from django.core import serializers
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

class profileView(TemplateView):
	template_name = 'blogapp/profile.html'
	
	def get(self, request, id):
		objectProfile = get_object_or_404(profile, id=int(id))
		return render(request, self.template_name, {'objectProfile': objectProfile})

	def post(self, request, id):
		print(request.POST)
		list_update =['first_name','last_name','phone','address','facebooke','github','twitter','status']

		profile.objects.filter(id=id).update(first_name=request.POST['first_name'])
		profile.objects.filter(id=id).update(last_name=request.POST['last_name'])
		profile.objects.filter(id=id).update(phone=request.POST['phone'])
		profile.objects.filter(id=id).update(address=request.POST['address'])
		profile.objects.filter(id=id).update(facebooke=request.POST['facebooke'])
		profile.objects.filter(id=id).update(github=request.POST['github'])
		profile.objects.filter(id=id).update(twitter=request.POST['twitter'])
		profile.objects.filter(id=id).update(status=request.POST['status'])
		objectProfile = get_object_or_404(profile, id=int(id))

		return render(request, self.template_name, {'objectProfile': objectProfile})
		
		