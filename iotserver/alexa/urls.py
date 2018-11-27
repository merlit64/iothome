# -*- coding: utf-8 -*-

"""alexa URL Configurations
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
# -*- coding: utf-8 -*-

