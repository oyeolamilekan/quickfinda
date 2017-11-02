from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.home_page, name='home_page'),
	url(r'^index/$', views.real_index, name='real_index'),
	url(r'^women-dresses/$',views.women_index,name='wemen'),
	url(r'^tvs/$', views.tv_index, name='tv_index'),
	url(r'^shirts/$', views.shirts, name='shirts'),
	url(r'^phones/$', views.index, name='index'),# 
	url(r'^minus_club/$', views.minus_club, name='minus_club'),
	url(r'^analytics/(?P<id>\d+)/$', views.number_of_clicks, name='analytics'),
	url(r'^feedback/$', views.feedback, name='feedback'),
	url(r'^laptops/$', views.laptops, name='laptops'),
 	url(r'^worker/$', views.despiration, name='worker'),
 	url(r'^download/$', views.engine_starter, name='engine_starter'),
 	url(r'^twitter_bot/$', views.twitter_bot, name='twitter_bot'),
 	url(r'^advanced_search/$', views.advanced_search, name='advanced_search'),
 	url(r'^men_watch/$',views.men_watch, name='men_watch'),
 	url(r'^women_watch/$',views.women_watch, name='women_watch')
   
]