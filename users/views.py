

from django.shortcuts import *
from django.views import generic
from users import models

from django.shortcuts import HttpResponse
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('user') #与html中表单中的name对应
        password = request.POST.get('pwd')
        #校验
        user_info = models.UserInfo.objects.filter(name=username,pwd=password).first()
        if user_info:
            request.session['user_session'] = {'id': user_info.id, 'name': user_info.name}
            return redirect("/home/")
        else:
            return render(request, 'register/login.html', {"error": "username or password error"})
    else:
        return render(request, 'register/login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('user')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        age = request.POST.get('age')
        pwd = request.POST.get('pwd')
        pwdconf = request.POST.get('pwdconfirm')
        if pwdconf == pwd:
            models.UserInfo.objects.create(name=name,email=email,mobile=mobile,age=age,pwd=pwd,subscribe=False)
        else:
            return render(request, 'register/signup.html', {"error": "passwords do not match!"})
    return render(request, 'register/signup.html')

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