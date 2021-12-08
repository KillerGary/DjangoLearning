# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request,'Login.html')


def login01_view(request):
    #接受表单请求参数
    uname=request.GET.get('uname','')
    pwd=request.GET.get('pwd','')
    #get()相当于一个字典，其中k指的是表单中name，value表示输入框中输入的值

    #判断
    if uname=='zhangsan' and pwd=='123':
          return HttpResponse('登陆成功！')

    return HttpResponse('登陆失败！')


