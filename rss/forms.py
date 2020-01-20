#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.core.validators import FileExtensionValidator

from .models import RSS


class RssForm(forms.ModelForm):
    ''' '''
    file = forms.FileField(
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=['rss'])])
    link = forms.URLField(required=False)

    class Meta:
        model = RSS
        fields = ['link']

    def clean(self):
        cleaned_data = super().clean()
        link = cleaned_data.get('link')
        file = cleaned_data.get('file')

        if not link and not file:
            raise forms.ValidationError('Inserire un URL o caricare un file')

        return cleaned_data
