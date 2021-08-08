from django.shortcuts import render
from blogapp.models.Post import Post
from blogapp.models.Setting import Vul
from django.views.generic import TemplateView


class indexView(TemplateView):
    def get(self, request, *args, **kwargs):
        xss = Vul.objects.filter(name="XSS").values()[0]["status"]
        object_list = Post.objects.raw(
            "select p.id, p.title, p.content, p.creat_time, p.images, a.username from blogapp_post as p left join blogapp_post_author_id as a1 on p.id = a1.post_id left join auth_user as a on a1.user_id = a.id;"
        )
        latest = object_list = Post.objects.raw(
            "select p.id, p.title, p.content, p.creat_time, p.images, a.username from blogapp_post as p left join blogapp_post_author_id as a1 on p.id = a1.post_id left join auth_user as a on a1.user_id = a.id limit 3;"
        )
        return render(
            self.request,
            "blogapp/index.html",
            {
                "object_list": object_list,
                "latest": latest,
                "xss": xss,
            },
        )
