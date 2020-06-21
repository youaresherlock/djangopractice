from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from booktest.models import BookInfo
# Create your views here.


class TestModelView1(View):
    """测试增改删
    create方法新增记录
    模型类.模型管理器.create()
    bookInfo.objects.create(
    btitle = '三国演义',
    bpub_date = '2019-6-7',
    bread = 100,
    bcomment = 200
    )
    """
    def get(self, request):
        book = BookInfo()
        book.btitle = '西游记'
        book.bpub_date = '2020-5-20'
        book.bread = 20
        book.bcomment = 30
        book.save()

        return HttpResponse('测试增改删')
