from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def set_cookie(request):
    """设置cookie"""
    request.session['itcast'] = 'heima'
    response = HttpResponse("set cookies")
    response.set_cookie("username", "clarence", 3600)
    return response


def get_cookie(request):
    """获取cookie"""
    cookies = request.COOKIES
    print(cookies)
    return HttpResponse("get cookies")

