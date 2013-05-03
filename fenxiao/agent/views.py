#coding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from  django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
def index(request):
     return render_to_response('agent/login.html',context_instance = RequestContext(request))
def add(request):
    a = User.objects.create_user(username='liukoo',password='liukoo')
    a.save()
    return HttpResponse(a)

