from os import name
from xml.etree.ElementTree import parse
from django.contrib.auth.models import User
from django.template.base import Parser
from django.utils import tree
from django.views.generic import TemplateView
from django.shortcuts import render
from lxml import etree
from blogapp.models.Post import Post
from blogapp.models.Tag import Tags
class requestpostView(TemplateView):
    template_name = "requestpost.html"
    def get(self, request):

        return render(request, self.template_name)

    def post(self, request):
        if request.FILES:
            xmlfile = request.FILES['xmlfile']
            parser = etree.XMLParser(load_dtd=True, resolve_entities=True)
            tree = etree.parse(xmlfile, parser=parser)
            root = tree.getroot()
            create=Post.objects.create(title=root[0].text, status=root[2].text, content=root[3].text)
            tag = Tags.objects.filter(name__in=root[1].text)
            create.tags.set(tag)
            create.author_id.add(request.user.id)
            
        return render(request, self.template_name)