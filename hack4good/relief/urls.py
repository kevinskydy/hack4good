from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

urlpatterns = patterns('relief.views',
	url(r'^$', TemplateView.as_view(template_name='relief/base.html')), 	
)