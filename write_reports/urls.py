from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<report_id>[0-9]+)/edit_report/$', views.edit_report, name='edit_report'),
    url(r'^create_report/$', views.create_report, name='create_report'),
    url(r'^(?P<report_id>[0-9]+)/delete_report/$', views.delete_report, name='delete_report'),
    url(r'^(?P<report_id>[0-9]+)$', views.show_detail_of_report, name='show_detail_of_report'),
]
