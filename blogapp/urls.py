from django.urls import path
from blogapp.views.post import post
from blogapp import views


urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    path('post/<id>/', views.post, name="post"),
    path('search/', views.search, name="search"), 
    path('setting/', views.setting , name="setting"),
   
]
