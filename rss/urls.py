#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from .views import *

urlpatterns = [
    path('add_RSS/', RSSLinkAddView.as_view(), name='add_rss'),
    path('show-rss-articles/<int:pk>/', RSSArticleView.as_view(), name='show-rss'),
    path('delete-rss/<int:pk>/', RSSDeleteView.as_view(), name="delete-rss"),
]
