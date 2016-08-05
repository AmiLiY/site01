# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.contrib.auth.views import login, logout_then_login


urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
]
