"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
# 导入 include 函数
from django.contrib import admin
from django.urls import path, include
# 以下代码注册自定义的路由转换器
from django.urls.converters import register_converter
from converters import MobileConverter
# 参数: 路由转换器，别名
register_converter(MobileConverter, "mobile")


urlpatterns = [
    # django默认就有的路由配置信息, 第一行不用管:
    path('admin/', admin.site.urls),

    # 添加如下的路由配置信息:
    # 设置子应用别名和子应用的子路由起别名 两种方法
    # path('', include(('子路由', '子应用名字'), namespace='总路由别名，可以随便命名')),
    # path(r'users/', include(('users.urls', "username"), namespace="username")),
    path(r'users/', include('users.urls')),
    path('', include('cookdemo.urls')),
    path('', include('classdemo.urls')),
    path('', include('booktest.urls')),
]