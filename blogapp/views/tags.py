from django.views.generic.base import TemplateView
from django.shortcuts import render
from blogapp.models.Post import Post
from django.views.generic import TemplateView

class tagsView(TemplateView):
    template_name = 'tags.html'

    def get(self, request, tag):
        tag_post = Post.objects.filter(tags__name=tag)

        return render(request, self.template_name, {'tag': tag, 'tag_post': tag_post})
