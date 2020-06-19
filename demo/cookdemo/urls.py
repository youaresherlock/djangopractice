from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path(r"^set_cookie/$", views.set_cookie),
    re_path(r"^get_cookie/$", views.get_cookie),
]