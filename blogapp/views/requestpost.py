import os
from django.views.generic import TemplateView
from django.shortcuts import render
from lxml import etree
from blogapp.models.Post import Post
from blogapp.models.Tag import Tags
from datetime import datetime
import requests
from django.utils.crypto import get_random_string

class requestpostView(TemplateView):
    template_name = "requestpost.html"
    VALID_KEY_CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789'
    def get(self, request):

        return render(request, self.template_name)

    def post(self, request):
        if request.FILES:
            xmlfile = request.FILES['xmlfile']
            parser = etree.XMLParser(load_dtd=True, resolve_entities=True)
            tree = etree.parse(xmlfile, parser=parser)
            root = tree.getroot()
            file = self.generate_file()
            with open("core/media/"+file, "wb") as img:
                res = requests.get(root[4].text)
                img.write(res.content)
            create=Post.objects.create(title=root[0].text, status=root[2].text, content=root[3].text, images=file)
            tag = Tags.objects.get(name=root[1].text)
            create.tags.add(tag.id)
            create.author_id.add(request.user.id)
            
        return render(request, self.template_name)

    def generate_file(self):
        dirname = datetime.now().strftime("uploads/%Y/%m/%d/")
        filename = get_random_string(10, self.VALID_KEY_CHARS) + ".jpg"

        filename = os.path.normpath(os.path.join(dirname,filename))
        if not os.path.exists("core/media/"+dirname):
            os.makedirs("core/media/"+dirname)
            return filename
        else:
            return filename