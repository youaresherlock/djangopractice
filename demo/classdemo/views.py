from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View


def my_decorator(func):
    def wrapper(request, *args, **kwargs):
        print('自定义装饰器被调用了')
        print('请求路径%s' % request.path)
        return func(request, *args, **kwargs)
    return wrapper


# 定义的Mixin扩展类
class FirstMixin(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        view = my_decorator(view)
        return view


class RegisterView(FirstMixin, View):
    # @method_decorator(my_decorator)
    def get(self, request):
        return HttpResponse("get")

    def post(self, request):
        return HttpResponse("post")
