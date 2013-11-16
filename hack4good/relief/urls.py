from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from views import *

urlpatterns = patterns('relief.views',
	#url(r'^$', TemplateView.as_view(template_name='relief/base.html')),
	url(r'^causes/$', CausesIndexView.as_view(), name='cause_index'),
	url(r'^relief_centers/(?P<cause_id>\w+)/$', ReliefCentersIndexView.as_view(), name='relief_center_index'),
	url(r'^goals/(?P<ctr_id>\w+)/$', GoalsIndexView.as_view(), name='goal_index')
)