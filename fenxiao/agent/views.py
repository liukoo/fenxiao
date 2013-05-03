#coding:utf-8
from django.shortcuts import render_to_response
from  django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
import fenxiao.settings
from django.contrib.auth import authenticate,login
def index(request):
            user_cache = authenticate(username='admin', password='admin')
            #如果成功返回对应的User对象，否则返回None(只是判断此用户是否存在，不判断是否is_active或者is_staff)
            if user_cache is None:
                msg ="您输入的用户名或密码不正确!"
            elif not user_cache.is_active or not user_cache.is_staff:
                msg ="您输入的用户名或密码不正确!"
            else:
                login(request,user_cache)
            return HttpResponse(msg)

