from blogapp.models.Userprofile import Userprofile as profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render
from lxml import etree
from io import StringIO


class profileView(LoginRequiredMixin, TemplateView):
	login_url = '/login'
	redirect_field_name = 'next'
	template_name = 'blogapp/profile.html'

	def get(self, request):
		id = request.user.id
		objectProfile = get_object_or_404(profile, id=id)
		return render(request, self.template_name, {'objectProfile': objectProfile})

	def post(self, request):
		id = request.user.id

		if request.FILES:
			xmlfile = request.FILES['xmlfile']

			parser = etree.XMLParser(load_dtd=True, resolve_entities=True)
			tree = etree.parse(xmlfile, parser=parser)
			root = tree.getroot() # Parse cac element vao mot array root

			profile.objects.filter(id=id).update(first_name=root[0].text)
			profile.objects.filter(id=id).update(last_name=root[1].text)
			profile.objects.filter(id=id).update(phone=int(root[2].text))
			profile.objects.filter(id=id).update(address=root[3].text)
			profile.objects.filter(id=id).update(facebooke=root[4].text)
			profile.objects.filter(id=id).update(github=root[5].text)
			profile.objects.filter(id=id).update(twitter=root[6].text)
			profile.objects.filter(id=id).update(status=root[7].text)				

		else:
			try:
			# Xu ly du lieu xml
				parser = etree.XMLParser(load_dtd=True, resolve_entities=True)
				tree = etree.parse(StringIO(request.POST['status']), parser=parser)
				tree.xinclude()
				profile.objects.filter(id=id).update(status=tree.getroot().text)
			except: 
				profile.objects.filter(id=id).update(status=request.POST['status'])

			profile.objects.filter(id=id).update(first_name=request.POST['first_name'])
			profile.objects.filter(id=id).update(last_name=request.POST['last_name'])
			profile.objects.filter(id=id).update(phone=request.POST['phone'])
			profile.objects.filter(id=id).update(address=request.POST['address'])
			profile.objects.filter(id=id).update(facebooke=request.POST['facebooke'])
			profile.objects.filter(id=id).update(github=request.POST['github'])
			profile.objects.filter(id=id).update(twitter=request.POST['twitter'])


		objectProfile = get_object_or_404(profile, id=id)

		return render(request, self.template_name, {'objectProfile': objectProfile})
		
		