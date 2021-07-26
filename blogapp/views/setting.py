from django.views.generic import ListView
from blogapp.models.Setting import Vul
from django.shortcuts import render
import base64, json, jwt

class settingView(ListView):
	# ListView mac dinh xu ly request GET nen khong can method GET
	template_name = 'setting.html'
	model = Vul
	nameVuls = Vul.objects.values('name')
	jwts = Vul.objects.filter(name="JWT").values('status')
	jwt_confusion = Vul.objects.filter(name="JWT_Key_Confusion").values('status')

	def post(self, request):
		cookie_check = request.COOKIES['auth']

		if self.jwt_confusion and not self.jwts:

			ext, fake = cookie_check.split('.',1)
			header = base64.urlsafe_b64decode(bytes(str(ext),'utf-8'))
			pubkey = json.loads(header.decode('utf-8'))    
			publickey = pubkey['publickey']

			from core.lib import jwt_vul
			cookie_decode = jwt_vul.decode(cookie_check, publickey)
			
		elif self.jwts:

			from core.lib import jwt_vul
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

			object_list = Vul.objects.all()

			return render(request, self.template_name, {'object_list': object_list,'msg':'Change is success!'})
		else:
			return render(request, self.template_name, {'msg': "You don't have permission"})