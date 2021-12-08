# coding=utf-8
"""DjangoLearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Hello/', views.index_view),
    url(r'^Login/', include('Login.urls')),#创建一个新的应用
    url(r'^runoob/', views.index_view2),
    url(r'^runoob2/', views.index_view3),#变量；
    url(r'^runoob3/', views.index_view4),#列表；采用用 . 索引下标取出对应的元素。
    url(r'^runoob4/', views.index_view5),#字典
    url(r'^index/', views.indexshow),#测试
]
