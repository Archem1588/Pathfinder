__author__ = 'hannahpark'

from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.map, name='map'),
    ]