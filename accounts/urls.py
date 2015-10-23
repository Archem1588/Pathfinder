__author__ = 'hannahpark'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    # url(r'^$', views.login, name='login'),
    url(r'^auth/$', views.auth_view, name='auth_view'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^loggedin/$', views.loggedin, name='loggedin'),
    url(r'^invalid/$', views.invalid_login, name='invalid_login')
]