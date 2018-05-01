from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^(?P<id>\d+)$', views.profile)
	url(r'^new', views.add)
	url(r'^(?P<id>\d+)$/edit', views.edit)
]