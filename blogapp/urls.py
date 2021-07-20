from django.urls import path
from blogapp.views.post import post
from blogapp import views
from blogapp.views.register import registerView



urlpatterns = [
    path('', views.index.index, name="index"),
    path('blog/', views.blog.blog, name="blog"),
    path('blog/<pid>/', views.blog.blog, name="blog"), # parameter 'pid' phai trung ten voi agrument 'pid' trong view blog
    path('post/<id>/', views.post.post, name="post"),
    path('search/', views.search.search, name="search"), 
    path('setting/', views.setting.setting , name="setting"),
    path('register/',registerView.as_view(), name="register"),
    path('login', views.login_view, name="user_login"),
    path('logout/', views.logout_view.logout_view, name="user_logout"),
    path('tag/<tag>/', views.tag.tags, name="tags"),
]
