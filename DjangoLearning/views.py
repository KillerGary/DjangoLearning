# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):

    return HttpResponse("Hello world!")


    #使用 django.http.HttpResponse() 来输出 "Hello World！"。
    #该方式将数据与视图混合在一起，不符合 Django 的 MVC 思想.



    #创建一个html名为runoob.html

    # 这里使用 render 来替代之前使用的 HttpResponse。render 还使用了一个字典 context 作为参数。
    # context 字典中元素的键值 hello 对应了模板中的变量 {{ hello }}。



def index_view2(request):
    context = {}
    context['hello'] = 'hello world!GaryChern!runoob!'
    return render(request,'runoob.html',context)


def index_view3(request):
    views_name = "GaryChern"
    return render(request,'runoob2.html',{"name":views_name})


def index_view4(request):
    view_list=["GaryChern0","GaryChern1","GaryChern2"]
    return render(request,'runoob3.html',{"view_list":view_list})


def index_view5(request):
    view_dict={'Name': 'GaryChern', 'Age': 25, 'Class': 'First'}
    return render(request,'runoob4.html',{"view_dict":view_dict})


def indexshow(request):
    return render(request,'index.html')