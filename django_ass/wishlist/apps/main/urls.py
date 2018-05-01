from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	url(r'^dashboard$', views.dashboard),
	url(r'^create$', views.create),
	url(r'^process$', views.process),
	url(r'^add$', views.add_wish),
	url(r'^remove$', views.remove_wish),
# 	url(r'^wish_items/(?P<id>\d+)$', views.wish_item)
# 	url(r'^wish_items/create$', views.add_wish),
]