from django.contrib import admin
from relief.models import (
						Cause, 
						ReliefCenter, 
						Goal, 
						Item, 
						ItemType
						)

class CauseAdmin(admin.ModelAdmin):
	pass

class ReliefCenterAdmin(admin.ModelAdmin):
	pass

class GoalAdmin(admin.ModelAdmin):
	pass

class ItemAdmin(admin.ModelAdmin):
	pass

class ItemTypeAdmin(admin.ModelAdmin):
	pass

admin.site.register(Cause, CauseAdmin)
admin.site.register(ReliefCenter, ReliefCenterAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemType, ItemTypeAdmin)