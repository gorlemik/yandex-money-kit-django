# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^yandex-money/', include('yandex_money.urls')),
]
