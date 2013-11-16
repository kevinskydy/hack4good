from django.views.generic import View
from django.shortcuts import render
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
			'centers': cause.reliefcenter_set.all()
		})

class GoalsIndexView(View):
	def get(self, request, *args, **kwargs):
		ctr = ReliefCenter.objects.get(id=kwargs['ctr_id'])
		return render(request, 'relief/goals_index.html', {
			'goals': ctr.goal_set.all()
		})

