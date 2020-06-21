"""
中间件执行顺序: 处理请求前从上到下, 处理请求后从下到上
"""


def my_middleware(get_response):
    print('init 被调用')

    def middleware(request):
        print('before request 被调用')
        response = get_response(request)
        print('after response 被调用')
        return response
    return middleware


def my_middleware2(get_response):
    print('init2 被调用')

    def middleware(request):
        print('before request 2 被调用')
        response = get_response(request)
        print('after response 2 被调用')
        return response
    return middleware


# 导入中间件的父类
from django.utils.deprecation import MiddlewareMixin


class TestMiddleware1(MiddlewareMixin):
    """
    1. process_request(self, request): 请求刚进来, 执行视图函数之前调用
    2. process_view(self, request, view_func, view_args, view_kwargs):
        URL路由匹配成功后, 执行视图函数之前调用, 拿到视图函数对象, 以及所有参数
    3. process_template_response(self, request, response):
        执行了render()渲染方法后调用
    4. process_exception(self, request, exception):
        执行视图函数中遇到异常时调用
    5. process_response(self, request, response):
        执行视图函数之后有响应时调用
    """
    # 启动Django程序, 初始化中间件时,自动调用一次,用于确定是否启用当前中间件
    def __init__(self, get_response=None):
        pass
    """自定义中间件"""
    def process_request(self, request):
        """处理请求前自动调用"""
        print('process_request1 被调用')

    def process_view(self, request, view_func, view_args, view_kwargs):
        # 处理视图前自动调用
        print('process_view1 被调用')

    def process_response(self, request, response):
        """在每个响应返回给客户端之前自动调用"""
        print('process_response1 被调用')
        return response

















