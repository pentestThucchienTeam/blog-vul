from blogapp.views.tags import tags
from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models.Post import Post
from blogapp.models.Setting import Vul
<<<<<<< HEAD
from blogapp.models.Tag import Tags
from django.core.paginator import Paginator

def blog(request, pid=None):
    xss = Vul.objects.filter(name="XSS").values()[0]['status']
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 2)
    listtag = Tags.objects.all()
=======
from django.core.paginator import Paginator

def blog(request, pid):
    xss = Vul.objects.filter(name="XSS").values()[0]['status']
    object_list = Post.objects.all()

    paginator = Paginator(object_list, 2)
>>>>>>> master
    # print(paginator.count)

    try:
        page_number = pid
        page_num_obj = paginator.page(page_number)
        print(page_num_obj.has_next)
        return render(request, 'blogapp/blog.html', {

            'object_list': object_list,
            'xss': xss,
            'paginator': paginator, 
<<<<<<< HEAD
            'page_num_obj': page_num_obj,
            'listtag':listtag
=======
            'page_num_obj': page_num_obj
>>>>>>> master
            }
        )
    except:
        page_number = 1
        page_num_obj = paginator.page(page_number)
        print(page_num_obj.has_next)
        return render(request, 'blogapp/blog.html', {

            'object_list': object_list,
            'xss': xss,
            'paginator': paginator, 
<<<<<<< HEAD
            'page_num_obj': page_num_obj,
            'listtag':listtag
=======
            'page_num_obj': page_num_obj
>>>>>>> master
            }
        )
