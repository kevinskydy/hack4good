from django.db import models
from datetime import date, datetime

# Create your models here.

class Cause(models.Model):
	name = models.CharField(max_length=128, default='Cause Name')
	created = models.DateTimeField(auto_now_add=True, default=datetime.now())

	def __unicode__(self):
		return "%s" % (self.name)

class ReliefCenter(models.Model):
	cause = models.ForeignKey('Cause')
	name = models.CharField(max_length=64, default='ReliefCenter Name')
	longitude = models.FloatField(blank=True, null=True)
	latitude = models.FloatField(blank=True, null=True)

	def __unicode__(self):
		return "%s" % (self.name)

class Goal(models.Model):
	relief_center = models.ForeignKey('ReliefCenter')
	target_date = models.DateField(default=date.today())

	@property
	def get_remaining_time(self):
		return datetime.now() - target_date

	def __unicode__(self):
		return "%s: %s" % (self.relief_center, self.target_date)

class Delivery(models.Model):
	item = models.ForeignKey('Item')
	quantity = models.IntegerField()
	arrival_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "%s: %d" % (self.item, self.quantity)

	class Meta:
		verbose_name_plural = 'deliveries'

class ItemType(models.Model):
	name = models.CharField(max_length=32, default='ItemType Name')

	def __unicode__(self):
		return "%s" % (self.name)

class Item(models.Model):
	goal = models.ForeignKey('Goal')
	item_type = models.ForeignKey('ItemType')
	quota = models.IntegerField(default=0)

	# @property
	def get_total_delivered(self):
		return reduce(lambda d, total: d.quantity + total, self.delivery_set.all, 0)

	@property
	def get_is_complete(self):
		return self.total_delivered == quota

	def __unicode__(self):
		return "%s: %s - %d" % (self.goal, self.item_type, self.quota)
