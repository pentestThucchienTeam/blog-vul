from django.views.generic import ListView,View
from django.views.generic.base import TemplateView
from blogapp.models.Setting import Vul
from django.shortcuts import render
import base64, json, jwt
from django.http import HttpResponse , HttpRequest
from django.template import engines
from django.contrib.auth import authenticate
from core.lib import jwt_vul


class settingView(ListView):
	# ListView mac dinh xu ly request GET nen khong can method GET
	template_name = 'setting.html'
	nameVuls = Vul.objects.values()[0]['status']
	jwt_confusion = Vul.objects.filter(name="JWT_Key_Confusion").values()[0]['status']
	
	def get(self, request):
		object_list = Vul.objects.all()
		ssti = Vul.objects.filter(name="SSTI").values()[0]['status']
		if ssti:
			engine = engines["django"]
			request.user.username = engine.from_string(request.user.username).render()
			object_list = Vul.objects.all()
			return render(request,self.template_name,{'object_list': object_list})
		else:
			return render(request,self.template_name,{'object_list': object_list})

	def post(self, request):
		object_list = Vul.objects.all()
		jwts = Vul.objects.filter(name="JWT").values()[0]['status']
		if request.user.username :
			cookie_check = request.COOKIES['auth']
			if self.jwt_confusion and not self.jwts:
				ext, fake = cookie_check.split('.',1)
				header = base64.urlsafe_b64decode(bytes(str(ext),'utf-8'))
				pubkey = json.loads(header.decode('utf-8'))    
				publickey = pubkey['publickey']
				cookie_decode = jwt_vul.decode(cookie_check, publickey)
				
			elif jwts:
				key = request.session['key']
				cookie_decode = jwt_vul.decode(cookie_check, key)

			else:
				
				key = request.session['key']
				cookie_decode = jwt.decode(cookie_check, key, algorithms="HS256")
			
			if cookie_decode['admin']:

				for _vuls in self.nameVuls:

					if request.POST[_vuls['name']] == "yes":
						Vul.objects.filter(name=_vuls['name']).update(status=True)
					else:
						Vul.objects.filter(name=_vuls['name']).update(status=False)

				
				return render(request, self.template_name, {'object_list':object_list,'msg':'Change is success!'})
			else:
				
				return render(request,self.template_name,{'object_list':object_list,'msg':"You don't have permission"})
				
		else:
			return render(request, self.template_name, {'object_list':object_list,'msg':'Please login to apply this change!'})