# 从 urls 模块中导入 re_path
from django.urls import re_path, path
# 从当前目录导入我们的视图模块 views
from . import views

app_name = "username"

# urlpatterns 是被 django 自动识别的路由列表变量
urlpatterns = [
    # 每个路由信息都需要使用 url 函数来构造
    # url (路径, 视图)
    re_path(r'^index/$', views.index),
    re_path(r'^say', views.say, name="say"),  # 定义子路由别名
    # re_path(r'^weather/([a-z]+)/(\d{4})', views.routerparams),
    # 给分组起名字 命名参数
    re_path(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})', views.routerparams),
    re_path(r'^formdata/$', views.formparams),
    re_path(r'^jsondata/$', views.get_body_json),
    re_path(r'^render/$', views.renderpage),
    # 在as_view->view->setup->dispatch 路径参数通过kwargs来传递, 需要在处理函数中接受
    # 这个关键字参数
    # 路由参数转换器: C:\Users\Clarence\Envs\django_pro\Lib\site-packages\django\urls\converters.py
    path('url_param/<mobile:phone_num>/', views.URLParamView.as_view()),
    path('resp_json/', views.JSONResponseView.as_view()),
    # 以下路由演示重定向
    path('index_page/', views.IndexView.as_view()),
    path('login_redirect/', views.LoginRedirectView.as_view()),
    path('download/', views.DownloadPictureView.as_view()),
]


"""
path: 使用路由转换器 path('url_param/<mobile:phone_num>/', views.URLParamView.as_view())
re_path: 所有正则需要自己书写 re_path(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})', views.routerparams)
url和re_path通过路径取参一样
"""