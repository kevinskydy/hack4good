from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('accounts.views', 
	url(r'^login$', login, { 'template_name': 'accounts/login.html' }, name='accounts_login'),
	url(r'^logout$', logout, name='accounts_logout'),
)