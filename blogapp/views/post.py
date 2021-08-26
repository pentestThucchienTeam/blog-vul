from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from .comment_form import CommentForm
from blogapp.models.Post import Post
from blogapp.models.Tag import Tags
from blogapp.models.Setting import Vul


class postView(TemplateView):

    template_name = "post.html"

    def get(self, request, id):
        form = CommentForm()
        postView.object_list = Post.objects.filter(status=1).order_by('-creat_time')[:5]
        postView.listtag = Tags.objects.all()
        postView.xss = Vul.objects.filter(name="XSS").values()[0]["status"]
        postView.sql = Vul.objects.filter(name="SQLI").values()[0]["status"]
        
        try:
            id1 = int(id) - 1 
            postView.pre_post = get_object_or_404(Post, id=id1)
        except:
            id1 = 1
            postView.pre_post = get_object_or_404(Post, id=id1)
        try:
            id1 = int(id) + 1 
            postView.next_post = get_object_or_404(Post, id=id1)
        except:
            id1 = 1
            postView.next_post = get_object_or_404(Post, id=id1)
        if self.sql:
            postView.post_render = Post.objects.raw("SELECT * FROM blogapp_post WHERE id = %s" % id)
        else:
            postView.post_render = get_object_or_404(Post, id=id)

        return render(
            request,
            self.template_name,
            {
                "object_list": self.object_list,
                "listtag": self.listtag,
                "post_render": self.post_render,
                "form": form,
                "xss": self.xss,
                "sql": self.sql,
                "pre_post": self.pre_post,
                "next_post": self.next_post,
            },
        )

    def post(self, request, id):
        postView.object_list = Post.objects.filter(status=1).order_by('-creat_time')[:5]
        postView.listtag = Tags.objects.all()
        postView.xss = Vul.objects.filter(name="XSS").values()[0]["status"]
        postView.sql = Vul.objects.filter(name="SQLI").values()[0]["status"]
        
        try:
            id1 = int(id) - 1 
            postView.pre_post = get_object_or_404(Post, id=id1)
        except:
            id1 = 1
            postView.pre_post = get_object_or_404(Post, id=id1)
        try:
            id1 = int(id) + 1 
            postView.next_post = get_object_or_404(Post, id=id1)
        except:
            id1 = 1
            postView.next_post = get_object_or_404(Post, id=id1)
        if self.sql:
            postView.post_render = Post.objects.raw("SELECT * FROM blogapp_post WHERE id = %s" % id)
        else:
            postView.post_render = get_object_or_404(Post, id=id)

        form = CommentForm(data=request.POST, author_id=request.user, post_id=self.post_render, email=request.user)
        if form.is_valid():
            form.save()

        return render(
            request,
            self.template_name,
            {
                "object_list": self.object_list,
                "listtag": self.listtag,
                "post_render": self.post_render,
                "form": form,
                "xss": self.xss,
                "sql": self.sql,
                "pre_post": self.pre_post,
                "next_post": self.next_post,
            },
        )
