from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^dashboard$', views.dashboard),
	url(r'^process$', views.process),
	url(r'^create$', views.create),
	url(r'^add_wish/(?P<id>\d+)$', views.add_wish),
	url(r'^rem_wish/(?P<id>\d+)$', views.rem_wish),
	url(r'^item/(?P<id>\d+)$', views.item),
	url(r'^logout$', views.logout),
	url(r'^delete$', views.delete)
	

]
