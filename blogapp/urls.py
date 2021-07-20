from blogapp.views.search import search
from blogapp.views import blog, index, register, tags
from django.urls import path
from blogapp.views.post import post
from blogapp import views
from django.urls import path, re_path

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('blog/', views.blog, name="blog"),
    path('blog/<pid>/', views.blog, name="blog"), # parameter 'pid' phai trung ten voi agrument 'pid' trong view blog
    path('post/<id>/', views.post, name="post"),
    path('search/', views.search.search, name="search"), 
    path('setting/', views.setting, name="setting"),
    path('register/', register.as_view(), name="register"),
    path('login', views.login_view, name="user_login"),
    path('logout/', views.logout_view, name="user_logout"),
    path('tag/<tag>/', tags.as_view(), name="tags"),
]
