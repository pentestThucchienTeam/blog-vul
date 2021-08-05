from blogapp.views.profile_form import ProfileForm
from blogapp.models.Userprofile import Userprofile as profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render
from django.core.files.storage import FileSystemStorage

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
			profile_update = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
			profile_update.save()
		else:
			profile_update = ProfileForm(request.POST, instance=request.user.profile)
			profile_update.save()
			# parser = etree.XMLParser(load_dtd=True, resolve_entities=True)
			# tree = etree.parse(xmlfile, parser=parser)
			# root = tree.getroot() # Parse cac element vao mot array root

			# Xu ly du lieu xml
				# parser = etree.XMLParser(load_dtd=True, resolve_entities=True)
				# tree = etree.parse(StringIO(request.POST['status']), parser=parser)
				# tree.xinclude()
				# profile.objects.filter(id=id).update(status=tree.getroot().text)


		objectProfile = get_object_or_404(profile, id=id)

		return render(request, self.template_name, {'objectProfile': objectProfile})
		
		