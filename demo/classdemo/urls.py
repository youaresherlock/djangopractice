from django.urls import re_path
from . import views

urlpatterns = [
    # re_path()中没有封装正则表达式的固定的规则, 所以re_path需要添加正则严格的开头和结束^$
    # 注意: 在给类视图注册子路由时,需要将类视图转成函数视图
    re_path(r"^register/$", views.RegisterView.as_view()),
]

"""
@classonlymethod:
    classonlymethod继承classmethod, 只能被类调用, 不能被实例对象调用
as_view(): 底层原理 
作用: 
    1. 将类视图转成函数视图 
    2. 传递客户端发送的参数 
    3. 进行请求分发
"""