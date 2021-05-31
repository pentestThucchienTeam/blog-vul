from django.urls import path
from blogapp import views


urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    path('post/<int:id>/', views.post),
]
