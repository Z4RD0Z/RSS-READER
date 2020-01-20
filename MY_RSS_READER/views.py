#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, RedirectView, TemplateView


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    pattern_name = 'homepage'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class LoginView(FormView):
    template_name = "login.html"
    success_url = reverse_lazy('homepage')
    form_class = AuthenticationForm

    def form_valid(self, form):
        """
            Provides the ability to login as a user with a username and password.
        """
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class HomeView(TemplateView):
    template_name = "rss/rss.html"
