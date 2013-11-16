from django.contrib import admin
from relief.models import (
						Cause, 
						ReliefCenter, 
						Goal, 
						Delivery, 
						Item, 
						ItemType
						)

class CauseAdmin(admin.ModelAdmin):
	list_display = ['name']

class ReliefCenterAdmin(admin.ModelAdmin):
	list_display = ['name', 'cause', 'longitude', 'latitude']

class GoalAdmin(admin.ModelAdmin):
	list_display = ['relief_center', 'target_date']

class DeliveryAdmin(admin.ModelAdmin):
	list_display = ['item', 'quantity', 'arrival_date']

class ItemAdmin(admin.ModelAdmin):
	list_display = ['goal', 'item_type', 'quota']

class ItemTypeAdmin(admin.ModelAdmin):
	list_display = ['name']

admin.site.register(Cause, CauseAdmin)
admin.site.register(ReliefCenter, ReliefCenterAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemType, ItemTypeAdmin)