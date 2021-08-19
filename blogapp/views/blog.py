from django.views.generic.base import TemplateView
from django.shortcuts import render
from blogapp.models.Post import Post
from blogapp.models.Setting import Vul
from blogapp.models.Tag import Tags
from django.core.paginator import Paginator


class blogView(TemplateView):
    template_name = "blog.html"

    def get(self, request, pid=None):
        xss = Vul.objects.get(name="XSS").status
        object_list = Post.objects.filter(status=1)
        lastest_post = Post.objects.all().order_by('-creat_time')[:5]
        paginator = Paginator(object_list, 2)
        listtag = Tags.objects.all()
        try:
            page_number = pid
            page_num_obj = paginator.page(page_number)
            return render(
                request,
                self.template_name,
                {
                    "object_list": object_list,
                    "xss": xss,
                    "paginator": paginator,
                    "page_num_obj": page_num_obj,
                    "listtag": listtag,
                    "lastest_post":lastest_post,
                },
            )
        except:
            page_number = 1
            page_num_obj = paginator.page(page_number)
            return render(
                request,
                self.template_name,
                {
                    "object_list": object_list,
                    "xss": xss,
                    "paginator": paginator,
                    "page_num_obj": page_num_obj,
                    "listtag": listtag,
                    "lastest_post":lastest_post,
                },
            )
