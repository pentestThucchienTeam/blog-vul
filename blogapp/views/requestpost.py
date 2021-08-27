import os
from django.views.generic import TemplateView
from django.shortcuts import render
from lxml import etree
from blogapp.models.Post import Post
from blogapp.models.Tag import Tags
from blogapp.models.Setting import Vul
from datetime import datetime
import requests
from django.utils.crypto import get_random_string
from defusedxml.ElementTree import parse


class requestpostView(TemplateView):
    template_name = "requestpost.html"
    VALID_KEY_CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789'

    def get(self, request):
        object_list = Post.objects.filter(author_id=request.user.id, status=2).order_by('-creat_time')
        return render(request, self.template_name,{'object_list': object_list})

    def post(self, request):
        xxe = Vul.objects.get(name='XXE').status
        ssrf = Vul.objects.filter(name="SSRF").values()[0]["status"]
        if request.FILES:
            xmlfile = request.FILES['xmlfile']
            if xxe:
                parser = etree.XMLParser(load_dtd=True, resolve_entities=True)
                tree = etree.parse(xmlfile, parser=parser)
            else:
                tree = parse(xmlfile)
            root = tree.getroot()
            file = self.generate_file()
            with open("core/media/"+file, "wb") as img:
                res = requests.get(root[3].text)
                img.write(res.content)
            create=Post.objects.create(title=root[0].text, status=2, content=root[2].text, images=file)
            create.author_id.add(request.user.id)
            tag = Tags.objects.filter(name=root[1].text)
            if tag:
                tagID = Tags.objects.get(name=root[1].text)
            else:
                tagID = Tags(name=root[1].text)
                tagID.save()
            create.tags.add(tagID.id)
            object_list = Post.objects.filter(author_id=request.user.id, status=2).order_by('-creat_time')
            return render(request, self.template_name, {'id': create.id, 'object_list': object_list})
        else:
            if not ssrf:
                with open('text/blacklist.txt', 'r') as file:
                    blacklist = [s.strip() for s in file.readlines()]
                url = self.request.POST.get("crawl")
                for x in blacklist:
                    if x in url:

                        return render(request, self.template_name,{"message":"Your URL does not match our rules. Please re-enter another URL"},status=403)        
            return render(request, self.template_name,)
        
    def generate_file(self):
        dirname = datetime.now().strftime("uploads/%Y/%m/%d/")
        filename = get_random_string(10, self.VALID_KEY_CHARS) + ".jpg"

        filename = os.path.normpath(os.path.join(dirname,filename))
        if not os.path.exists("core/media/"+dirname):
            os.makedirs("core/media/"+dirname)
            return filename
        else:
            return filename