from django.views.generic import View
from django.shortcuts import render
from django.conf import settings
from models import *

class CausesIndexView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'relief/causes_index.html', {
			'causes': Cause.objects.all()
		})

class ReliefCentersIndexView(View):
	def get(self, request, *args, **kwargs):
		cause = Cause.objects.get(id=kwargs['cause_id'])
		return render(request, 'relief/relief_centers_index.html', {
			'cause': cause,
			'centers': cause.reliefcenter_set.all(),
			'base_url': settings.BASE_URL
		})

# class ReliefCenterView(View):
# 	def get(self, request, *args, **kwargs):
# 		return render(request, 'relief/relief_center_view.html', {
# 			'center': ReliefCenter.objects.get(id=kwargs['ctr_id'])
# 		})

class GoalsIndexView(View):
	def get(self, request, *args, **kwargs):
		ctr = ReliefCenter.objects.get(id=kwargs['ctr_id'])
		return render(request, 'relief/goals_index.html', {
			'ctr': ctr
		})

class GoalView(View):
	def get(self, request, *args, **kwargs):
		goal = Goal.objects.get(id=kwargs['goal_id'])
		return render(request, 'relief/goal_view.html', {
			'base_url': settings.BASE_URL,
			'goal': goal
		})
