from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^quotes$', views.quotes),
	url(r'^process$', views.process),
	url(r'^add_to_list/(?P<id>\d+)$', views.add_to_list),
	url(r'^rem_from_list/(?P<id>\d+)$', views.rem_from_list),
	url(r'^user$', views.profile),
	url(r'^logout$', views.logout)
	

]
