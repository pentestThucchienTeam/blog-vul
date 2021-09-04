from genericpath import exists
from django.views.generic import TemplateView
import os
import re
import mimetypes
from django.http import FileResponse, Http404
from django.views import View
from blogapp.models.Setting import Vul


class avatarView(View):
	def get(self, request):		
		fileName = request.GET['image']
		Ptraversal = Vul.objects.filter(name="Path travesal").values()[0]["status"]
		if not Ptraversal:
			pattern ="^[A-Za-z0-9\.\-_]+$"
			check = re.match(pattern, fileName)
			if not check:			
				raise Http404("Path is invalid!")
		uploadsFolder = "/code/core/media/uploads"
		fullPath = os.path.normpath(os.path.join(uploadsFolder, fileName))
		if not exists(fullPath):
			raise Http404
		content_type, encoding = mimetypes.guess_type(str(fullPath))
		content_type = content_type or 'application/octet-stream'
		response = FileResponse(open(fullPath, 'rb'), content_type=content_type)
		if encoding:
			response.headers["Content-Encoding"] = encoding
		
		return response