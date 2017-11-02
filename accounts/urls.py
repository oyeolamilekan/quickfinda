from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout,password_change,password_change_done,password_reset,password_reset_done,password_reset_confirm,password_reset_complete

urlpatterns = [
	url(r'^$', login, name='login'),
	url(r'^password-change/$',password_change,{'template_name':'registration/password_change_for.html'},name="password_change"),
    url(r'^passowrd-change/done/$',password_change_done,{'template_name':'registration/password_change_don.html'},name="password_change_done"),
	url(r'^logout/$', logout,{'template_name':'registration/logged_ou.html'}, name='logout'),
	url(r'^stream/$', views.stream, name='stream'),
	url(r'^sub/$', views.subscribe, name='subscribe'),
	url(r'^register/$', views.register, name='register'),
	url(r'^password-reset/$',password_reset,name='password_reset'),
    url(r'^password-reset/done/$',password_reset_done,name="password_reset_done"),
    url(r'^password-reset/confirm/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',password_reset_confirm,name="password_reset_confirm"),
    url(r'^password-reset/complete/$',password_reset_complete,name="password_reset_complete"),
]