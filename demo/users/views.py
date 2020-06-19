import os
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.views import View
from demo import settings


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
    print(city, year)
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
        # content响应体 content_type响应体数据类型, 默认text/html status状态码,默认200
        return HttpResponse("提取路径参数")


class DownloadPictureView(View):
    """下载图片
    """
    def get(self, request):
        try:
            data = request.GET
            file_name = data.get("file_name")
            image_path = os.path.join(settings.BASE_DIR, "static_files/{}".format(file_name))
            with open(image_path, "rb") as f:
                image_data = f.read()
            return HttpResponse(image_data, content_type="image/png")
        except Exception as e:
            print(e)
            return HttpResponse(str(e))


class Response1View(View):
    """演示HttpResponse
    提示:
        默认HttpResponse响应html字符串, 但是如果我们要响应html字符串以外的数据
        该如何实现?
        eg: 响应图片
        HttpResponse(响应体: 图片的原始数据, content_type='image/jpg)
        def read_img(request):
            try:
            data = request.GET
            file_name = data.get("file_name")
            image_path = os.path.join(settings.BASE_DIR, "static/resume/images/{}".format(file_name)
            with open(image_path, 'rb') as f:
                image_data = f.read()
            return HttpResponse(image_data, content_type="image/png")
        except Exception as e:
            print(e)
            return HttpResponse(str(e))
    """

    def get(self, request):
        return HttpResponse("演示HttpResponse")


class JSONResponseView(View):
    """演示JsonResponse
    GET http://127.0.0.1:8000/users/resp_json/
    """
    def get(self, request):
        """返回JSON数据"""
        dict_data = {
            'name': 'clarence',
            'age': 18
        }
        # safe = false, content可以是个列表
        return JsonResponse(dict_data)


class IndexView(View):
    """"首页视图
    GET http://127.0.0.1:8000/users/index_page/
    """
    def get(self, request):
        return HttpResponse("假装这是个首页")


class LoginRedirectView(View):
    """测试成功登陆后，进入首页的效果
    POST http://127.0.0.1:8000/users/login_redirect/
    """
    def post(self, request):
        # 如果用户登陆成功后，将用户引导到首页
        return redirect('/users/index_page/')




















