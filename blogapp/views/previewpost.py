from django.http.response import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.base import TemplateView
from blogapp.models.Post import Post
from blogapp.models.Tag import Tags


class preView(TemplateView):

    template_name = "preview.html"

    def get(self, request, id):
       
        preView.object_list = Post.objects.filter(status=1).order_by('-creat_time')[:5]
        preView.listtag = Tags.objects.all()
        preView.post_render = get_object_or_404(Post, id=id)
        print(preView.post_render.status)
        if preView.post_render.status != '2':
            raise Http404 
        else:
            return render(
                request,
                self.template_name,
                {
                    "object_list": self.object_list,
                    "listtag": self.listtag,
                    "post_render": self.post_render,             
                }
            )

    def post(self, request, id):
        preView.object_list = Post.objects.filter(status=1).order_by('-creat_time')[:5]
        preView.listtag = Tags.objects.all()
        preView.post_render = get_object_or_404(Post, id=id)
        Post.objects.filter(id=id).update(status=2)
        return redirect('/requestpost/')
    