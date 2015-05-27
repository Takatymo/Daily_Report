# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Report

# Create your forms here.
class form_for_edit(ModelForm):
    class Meta:
        model = Report
        fields = ('title', 'content')
