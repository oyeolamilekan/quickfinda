from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$',views.home_page,name='home_page'),
	url(r'^index/$',views.index,name='index'),
	url(r'^(?P<ads>\d+)/$', views.click_by, name='ads'),
	url(r'^dashboard/$', views.dash, name='dash'),
	url(r'^data_set/$', views.loaded, name='data_set'),
	url(r'^pay_val/$', views.payment_val, name='payment_val'),
	url(r'^ads_upload/$', views.upload_ads, name='upload_ads'),
	url(r'^edit_ads/(?P<id>\d+)/$', views.edit_ads, name='edit_ads'),
	url(r'^reactivation/$', views.reactivate_payment_val, name='reactivate_payment_val'),
]