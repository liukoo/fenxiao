#coding:utf-8
from django.shortcuts import render_to_response
from  django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
import fenxiao.settings
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
def index(request):
     msg =""
     user_cache = authenticate(username='admin', password='admin')
     #如果成功返回对应的User对象，否则返回None(只是判断此用户是否存在，不判断是否is_active或者is_staff)
     if user_cache is None:
        msg ="您输入的用户名或密码不正确!"
     elif not user_cache.is_superuser:
            msg ="您不是管理员!"
     else:
            login(request,user_cache)
     return HttpResponse(msg)
def add(request):
    msg = User.objects.create(username='liukoo',password='liukoo')
    return HttpResponse(msg)

