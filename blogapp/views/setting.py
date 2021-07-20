from django.views.generic import ListView
from blogapp.models.Setting import Vul
from django.shortcuts import render

class settingView(ListView):
	
	template_name = 'setting.html'
	model = Vul
	nameVuls = Vul.objects.values('name')

	def post(self, request):
		for _vuls in self.nameVuls:
			
			if request.POST[_vuls['name']] == "yes":
				Vul.objects.filter(name=_vuls['name']).update(status=True)
			else:
				Vul.objects.filter(name=_vuls['name']).update(status=False)

		object_list = Vul.objects.all()

		return render(request, self.template_name, {'object_list': object_list})