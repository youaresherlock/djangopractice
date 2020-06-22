from datetime import date

from django.db.models import F
from django.db.models import Q
from django.db.models import Sum
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from booktest.models import BookInfo, HeroInfo
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

    # save方法新增记录
    # def get(self, request):
    #     book = BookInfo()
    #     book.btitle = '西游记'
    #     book.bpub_date = '2020-5-20'
    #     book.bread = 20
    #     book.bcomment = 30
    #     book.save()
    #
    #     return HttpResponse('测试增改删')

    # 修改: save, update
    # def get(self, request):
        # save
        # book = BookInfo.objects.get(id=5)
        # book.btitle = '西游记后传'
        # book.save()
        # update 模型对象.objects.filter('条件').update(模型属性=新值)
        # BookInfo.objects.filter(id=6).update(btitle='三国志')

        # 删除
        # 模型对象 = 模型类.objects.get()
        # 模型对象.delete()
        # 模型类.objects.filter().delete()
        # 逻辑删除
        # book = BookInfo.object.filter(pk=5)
        # book.is_delete = False
        # book.save()

    # 查询
    # def get(self, request):
        # 查询指定记录
        # 模型类.objects.get(条件)
        # book = BookInfo.objects.get(id=1)
        # print(book.btitle)

        # 查询所有记录
        # 模型类.objects.all()
        # books = BookInfo.objects.all()
        # 查询所有记录个数 模型类.objects.all().count()
        # 查询满足条件记录的个数
        # queryset才有count()方法
        # print(BookInfo.objects.filter(is_delete=False).count())

    # 过滤查询
    # def get(self, request):
        # 模型类.objects.filter(属性名称__比较运算符=值)
        # 1. 查询书名为'天龙八部'的书籍
        # books = BookInfo.objects.filter(btitle__exact="天龙八部")

        # 2. 查询书名包含"湖"的书籍
        # books = BookInfo.objects.filter(btitle__contains="湖")

        # 3. 查询书名以"部"结尾的书籍
        # books = BookInfo.objects.filter(btitle__endswith="部")

        # 4. 查询书名不为空的数据
        # BookInfo.objects.filter(btitle__isnull=False)

        # 5. 查询编号为1或3或5的书籍
        # BookInfo.objects.filter(id__in=[1, 3, 5])

        # 6. 查询编号大于3的书籍
        # lt小于 lte小于等于
        # BookInfo.objects.filter(id__gt="3")

        # 7. 查询id不等于3
        # exclude: 查询指定的条件以外的数据
        # filter: 查询满足指定条件的数据
        # BookInfo.objects.exclude(id=3)

        # 查询1980年发表的书籍
        # books = BookInfo.objects.filter(bpub_date__year=1980)

        # 查询1990年1月1日后发表的书籍
        # books = BookInfo.objects.filter(bpub_date__gt="1990-1-1")
        # books = BookInfo.objects.filter(bpub_date__gt=date(1990, 1, 1))

    # F和Q查询
    # def get(self, request):
        # F查询 对模型内的两个属性进行比较
        # 模型类.objects.filter(属性名称__比较运算符=F(属性名))
        # 1. 查询阅读量大于评论量的书籍
        # books = BookInfo.objects.filter(bread__gt=F('bcomment'))

        # 2. 查询阅读量大于2倍评论量的书籍
        # books = BookInfo.objects.filter(bread__gt=F('bcomment') * 2)

        # 查询阅读大于评论, 并且名字含有部
        # books = BookInfo.objects.filter(bread__gt=F('bcomment'), btitle__contains="部")

        # Q查询
        # Q(属性名__运算符=值)|Q(属性名__运算符=值)  逻辑或/逻辑非
        # 查询阅读量大于20或者编号小于3的图书
        # BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt=3))


    # 聚合查询 聚合函数 Avg、Count、Max、Min、SUM
    # 模型类.objects.aggregate(聚合函数(属性))
    # def get(self, request):
        # 1.统计图书信息总的阅读量
        # BookInfo.objects.aggregate(Sum('bread'))

    # 排序查询 模型类.objects.filter('条件').order_by('模型属性')
    # 默认正序, 倒序 模型类.objects.filter('条件').order_by('-模型属性')
    # def get(self, request):
        # 查询书名不为空的图书, 按照阅读量正序
        # books = BookInfo.objects.filter(btitle__isnull=False).order_by('bread')

        # 1. 查询编号为1的图书中所有人物信息 固定语法
        # 一查多
        # book = BookInfo.objects.get(id=1)
        # heros = book.heroinfo_set.all()
        # print(heros)
        # 多查一
        # hero = HeroInfo.objects.get(id=1)
        # hero.hbook

    # QuerySet 查询集 惰性执行
    def get(self, request):
        pass


class BooksView(View):
    def get(self, request):
        books = BookInfo.objects.all()
        context = {
            "books": books
        }
        return render(request, "index.html", context)













