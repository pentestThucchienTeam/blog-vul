import os
from django.views.generic import TemplateView
from django.shortcuts import render
from lxml import etree
from blogapp.models.Post import Post
from blogapp.models.Tag import Tags
from blogapp.models.Setting import Vul
from datetime import datetime
import requests
from urllib.parse import urlparse
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
        ssrf = Vul.objects.filter(name="SSRF").values()[0]["status"]
        if request.FILES:
            create = self.requestxml(xxe)
        else:
            if not ssrf:
                url = self.request.POST.get("crawl")
                blacklist = requestpostView.readfile()
                for x in blacklist:
                    if x in url:
                        return render(request, self.template_name,{"message":"Your URL does not match our rules. Please re-enter another URL"},status=403)    
            create = self.requesturl(xxe)
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

    def readfile():
        with open('text/blacklist.txt', 'r') as file:
                blacklist = [s.strip() for s in file.readlines()]
        return blacklist

    def requesturl(self, xxe):
        url = self.request.POST.get("crawl")
        url_parse = urlparse(url)
        url_parse = url_parse.scheme + '://' + url_parse.netloc
        crawl = requests.get(url)
        soup = BeautifulSoup(crawl.content, 'html5lib')
        imgdb= '/uploads/2021/05/31/postimages.jpg'
        fulltag=soup.body.find_all(["div","main","section","p"],
        class_ = ["post-content",
                "td-post-content",
                "section",
                "markdown-body",
                "ui pilled segment md",
                "md-contents article-content__body my-2 flex-fill default",
                "aq ar as at au fl aw w"])
        for i in soup.body.find_all('img', src=True):                
            if '//' not in i['src']:
                file = self.generate_file()
                with open("core/media/"+file, "wb") as img:
                    res = requests.get(url_parse+i['src'])
                    img.write(res.content)
                i['src'] = '/media/' + file               
        content = ""
        for i in fulltag:
            content += str(i)
        create= Post.objects.create(title=soup.title.text,status=2, content=content, images= imgdb)
        create.author_id.add(self.request.user.id)
        return create

    def requestxml(self, xxe):
        xmlfile = self.request.FILES['xmlfile']
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
        create.author_id.add(self.request.user.id)
        tag = Tags.objects.filter(name=root[1].text)
        if tag:
            tagID = Tags.objects.get(name=root[1].text)
        else:
            tagID = Tags(name=root[1].text)
            tagID.save()
        create.tags.add(tagID.id)
        return create