from django.contrib import admin
from .models import *

@admin.register(Goal)
class AdminGoal(admin.ModelAdmin):

    list_display =(
        'name',
        'startdate',
        'enddate',
        'totaltime',
        'reason',
    )

@admin.register(Task)
class AdminTask(admin.ModelAdmin):

    list_display = (
        'goal',
        'goal_name',
        'starttime',
        'duration',
    )

    def goal_name(self,obj):
        return obj.goal.name

admin.register(Goal)

# Register your models here.
