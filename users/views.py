import json
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import *
from django.views import generic
from users import models
from django import forms
from .forms import loginForm, signUpForm
from django.core.validators import RegexValidator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import HttpResponse
# Create your views here.


def login(request):
    if request.method=="GET":
        form = loginForm()
        print(form.errors)
        return render(request, 'register/login.html', {'form': form})
    form = loginForm(data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user_object = models.UserInfo.objects.filter(name=username,pwd=password).first()
        print(user_object)
        if user_object:
            request.session['user_session'] = {'id': user_object.id, 'name': user_object.name}
            request.session.set_expiry(60*60*24*7)
            return redirect("/home/")
        else:
            return render(request, 'register/login.html', {"form":form,"error": "username or password error"})
    else:
        # print(form.errors)
        return render(request, 'register/login.html', {'form': form})

    # if request.method == 'POST':
    #     username = request.POST.get('user') #与html中表单中的name对应
    #     password = request.POST.get('pwd')
    #     #校验
    #     user_info = models.UserInfo.objects.filter(name=username,pwd=password).first()
    #     if user_info:
    #         request.session['user_session'] = {'id': user_info.id, 'name': user_info.name}
    #         return redirect("/home/")
    #     else:
    #         return render(request, 'register/login.html', {"error": "username or password error"})
    # else:
    #     return render(request, 'register/login.html')

def signup(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            mobile = form.cleaned_data.get('mobile')
            age = form.cleaned_data.get('age')
            pwd = form.cleaned_data.get('password')
            pwdconf = form.cleaned_data.get('password_confirm')
            filterResult_username = models.UserInfo.objects.filter(name=name).first()
            filterResult_email = models.UserInfo.objects.filter(email=email).first()
            if filterResult_username:
                return render(request,'register/signup.html',{"form":form,"error": "Username exists!"})
            if filterResult_email:
                return render(request,'register/signup.html',{"form":form,"error": "Email exists!"})
            if pwdconf == pwd:
                user = models.UserInfo.objects.create(name=name,email=email,mobile=mobile,age=age,pwd=pwd,subscribe=False)
                user.save()
                return redirect('/users/success_signup/')
            else:
                return render(request, 'register/signup.html', {"form":form,"error": "passwords do not match!"})
        else:
            # print(form.errors)
            return render(request, 'register/signup.html', {'form': form})
    form = signUpForm()
    return render(request, 'register/signup.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('home')

def login_signup(request):
    return render(request, "register/login_signup.html")

def success_signup(request):
    return render(request,"register/success_signup.html")

def index(request):
    queryset = [
        {"name": "root", "phone": "11111111", "city": "上海"},
        {"name": 2, "phone": "11111111", "city": "上海"},
        {"name": 3, "phone": "11111111", "city": "上海"},
        {"name": 4, "phone": "11111111", "city": "上海"},
    ]
    # 2通过页面渲染返回用户，表格
    return render(request, 'index_admin.html', {"data": queryset})


def home(request):
    user_session = request.session.get('user_session')

    return render(request,"home.html",{"user_session":user_session})


def user_list(request):
    #1、数据库获取用户列表
    data = ["sihan","mia","ruize"]
    #2、打开文件并读取内容
    #3、模板渲染——文本替换
    #字典值与html模板中的名称对应
    return render(request,"user_list.html",{"message":"user——list","data_list":data})


def phone_list(request):
    #1\获取数据
    queryset = [
        {"id": 1, "phone":"11111111", "city":"上海"},
        {"id": 2, "phone": "11111111", "city": "上海"},
        {"id": 3, "phone": "11111111", "city": "上海"},
        {"id": 4, "phone": "11111111", "city": "上海"},
    ]
    #2通过页面渲染返回用户，表格
    return render(request,'phone_list.html',{"data":queryset})