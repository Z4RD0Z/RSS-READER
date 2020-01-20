#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from ..models import RSS

register = template.Library()


@register.inclusion_tag('templatetags/user_rss.html')
def show_all_user_rss(user):
    if user.id == None:
        pass
    else:
        user_rss = RSS.objects.filter(user=user)
        return {'user_rss': user_rss}
