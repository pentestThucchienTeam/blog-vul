import os
from django.http.response import Http404
from django.views.generic import TemplateView
from django.shortcuts import render
from lxml import etree
from blogapp.models.Post import Post
from blogapp.models.Tag import Tags
from blogapp.models.Setting import Vul
from datetime import datetime
import requests
from urllib.parse import urlparse
import re
from bs4 import BeautifulSoup
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
        else:
            url = self.request.POST.get("crawl")
            url_parse = urlparse(url)
            url_parse = url_parse.scheme + '://' + url_parse.netloc
            crawl = requests.get(url)
            soup = BeautifulSoup(crawl.content, 'html5lib')
            body = soup.body
            for i in body.find_all('img', src=True):
                if 'http' not in i['src']:
                    file = self.generate_file()
                    with open("core/media/"+file, "wb") as img:
                        res = requests.get(url_parse+i['src'])
                        img.write(res.content)
                else:
                    file = self.generate_file()
                    with open("core/media/"+file, "wb") as img:
                        res = requests.get(i['src'])
                        img.write(res.content)
                i['src'] = '/media/' + file
            p_tag = body.find_all(['p','pre','span'])
            content = ""
            for i in p_tag:
                content += str(i)

            create= Post.objects.create(title="aaaa",status=2, content=content)
            create.author_id.add(request.user.id)


        object_list = Post.objects.filter(author_id=request.user.id, status=2).order_by('-creat_time')
        return render(request, self.template_name, {'id': create.id, 'object_list': object_list})

    def generate_file(self):
        dirname = datetime.now().strftime("uploads/%Y/%m/%d/")
        filename = get_random_string(10, self.VALID_KEY_CHARS) + ".jpg"

        filename = os.path.normpath(os.path.join(dirname,filename))
        if not os.path.exists("core/media/"+dirname):
            os.makedirs("core/media/"+dirname)
            return filename
        else:
            return filename