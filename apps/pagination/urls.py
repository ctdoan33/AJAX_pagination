from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^page/(?P<id>\d+)', views.page),
    url(r'^search', views.search),
]