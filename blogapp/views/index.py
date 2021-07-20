from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from blogapp.models.Post import Post
from blogapp.models.Setting import Vul
class index(TemplateView):
    template_name='blogapp/index.html'
    def index(sefl,request):
        xss = Vul.objects.filter(name="XSS").values()[0]['status']
        object_list = Post.objects.raw('select p.id, p.title, p.content, p.creat_time, p.images, a.username from blogapp_post as p left join blogapp_post_author_id as a1 on p.id = a1.post_id left join auth_user as a on a1.user_id = a.id;')
        latest = object_list = Post.objects.raw('select p.id, p.title, p.content, p.creat_time, p.images, a.username from blogapp_post as p left join blogapp_post_author_id as a1 on p.id = a1.post_id left join auth_user as a on a1.user_id = a.id limit 3;')
        args = {'object_list': object_list, 'latest': latest, 'xss': xss,}
        return render(request, sefl.template_name, args )
