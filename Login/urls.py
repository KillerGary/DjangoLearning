# coding=utf-8

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.login_view),#创建一个新的应用
]