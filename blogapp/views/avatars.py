from genericpath import exists
import os
from decouple import config
import mimetypes
import os
from django.http import FileResponse, Http404
from django.views import View


class avatarView(View):
	def get(self, request):
		fileName = request.GET['image']
		uploadsFolder = config("avatarLink")
		fullPath = os.path.normpath(os.path.join(uploadsFolder, fileName))
		if not exists(fullPath):
			raise Http404
		content_type, encoding = mimetypes.guess_type(str(fullPath))
		content_type = content_type or 'application/octet-stream'
		response = FileResponse(open(fullPath, 'rb'), content_type=content_type)
		if encoding:
			response.headers["Content-Encoding"] = encoding
		
		return response