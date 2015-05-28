"""daily_report URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^write_reports/', include('write_reports.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^log_in/$', 'django.contrib.auth.views.login',
        {'template_name': 'write_reports/log_in.html'}, name='log_in'),
    url(r'^log_out/$', 'django.contrib.auth.views.logout',
        {'template_name': 'write_reports/log_out.html'}, name='log_out')
]
