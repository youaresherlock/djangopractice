import json
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views import View


def renderpage(request):
    """模拟前后端不分离,返回页面"""
    context = {
        'city': 'beijing'
    }
    return render(request, 'index.html', context)


# 通过查询字符串传参
def index(request):
    """
    index视图
    :param request: 包含了请求信息的请求对象
    :return: 响应对象
    """
    # 从请求对象中提取查询字符串时, 跟请求方式没有任何的关系
    print(request.GET)
    return HttpResponse("hello the world!")


def say(request):
    url = reverse("username:say")
    print(url)
    return HttpResponse("say")


# 通过URL路径传参
def routerparams(request, city, year):
    print(city)
    print(year)
    return HttpResponse("router")


def formparams(request):
    """表单传参"""
    # < QueryDict: {'user': ['manu'], 'password': ['123']} >
    print(request.POST)
    return HttpResponse("form params")


# 非表单类型传值的方式
def get_body_json(request):
    """定义一个函数,接受json数据"""
    json_bytes = request.body
    json_str = json_bytes.decode()
    dic = json.loads(json_str)
    print(dic.get("username"))
    print(dic.get("password"))

    # 补充: 获取请求头数据
    print(request.META['CONTENT_TYPE'])
    print(request.user)  # 没有登录为匿名用户, 登录为登录用户
    print(request.method)
    print(request.path)
    print(request.COOKIES)
    response = HttpResponse("OK")
    response.set_cookie("username", "clarence", 3600)
    return response


class URLParamView(View):

    def get(self, request, phone_num):
        print(phone_num)
        return HttpResponse("提取路径参数")

