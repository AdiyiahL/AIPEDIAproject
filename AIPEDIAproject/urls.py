"""AIPEDIAproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.http import HttpResponse
from django.shortcuts import HttpResponse
from django.urls import path, include, re_path
from django.views.static import serve

from AIPEDIAproject.settings import MEDIA_ROOT
from users.views import *
from content.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls',namespace='users')),
    path('index/',index),
    path('content/',include('content.urls',namespace='content')),
    path('home/',home),
    re_path(r'^media/(?P<path>.*)',serve, {'document_root': MEDIA_ROOT})

    # 验证码尝试
    # path('captcha/', include('captcha.urls')),
]
