from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^dashboard$', views.dashboard),
    url(r'^add_post$', views.add_post),
    url(r'^add_fav/(?P<id>\d+)$', views.add_wall),
    url(r'^remove_fav/(?P<id>\d+)$', views.remove_wall),
    url(r'^users/(?P<id>\d+)$', views.profile)
]