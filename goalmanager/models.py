from django.db import models


class Goal(models.Model):
    name = models.CharField(max_length=200)
    startdate = models.IntegerField()
    enddate = models.IntegerField()
    totaltime = models.IntegerField(default=0)
    reason = models.CharField(max_length=500)


class Task(models.Model):
    goal = models.ForeignKey(Goal,on_delete=models.CASCADE,null=True)
    starttime = models.IntegerField(null=True)
    duration = models.IntegerField()


# Create your models here.
