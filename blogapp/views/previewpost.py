from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from .comment_form import CommentForm
from blogapp.models.Post import Post
from blogapp.models.Tag import Tags
from blogapp.models.Setting import Vul


class preView(TemplateView):

    template_name = "post.html"

    def get(self, request, id):
        # form = CommentForm()
        preView.object_list = Post.objects.all().order_by('-creat_time')[:5]
        preView.listtag = Tags.objects.all()
        # preView.xss = Vul.objects.filter(name="XSS").values()[0]["status"]
        # preView.sql = Vul.objects.filter(name="SQLI").values()[0]["status"]
        # try:
        #     preView.pre_post = get_object_or_404(Post, id=(int(id) - 1))
        # except:
        #     preView.pre_post = get_object_or_404(Post, id=id)
        # try:
        #     preView.next_post = get_object_or_404(Post, id=(int(id) + 1))
        # except:
        #     preView.next_post = get_object_or_404(Post, id=id)
        # if self.sql:
        #     preView.post_render = Post.objects.raw("SELECT * FROM blogapp_post WHERE id = %s" % id)
        # else:
        preView.post_render = get_object_or_404(Post, id=id)

        return render(
            request,
            self.template_name,
            {
                "object_list": self.object_list,
                "listtag": self.listtag,
                "post_render": self.post_render,
                # "form": form,
                # "xss": self.xss,
                # "sql": self.sql,
                # "pre_post": self.pre_post,
                # "next_post": self.next_post,
            },
        )

