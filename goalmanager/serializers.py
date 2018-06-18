from rest_framework import serializers
from .models import *


class GoalSerializer(serializers.Serializer):
    name=serializers.CharField()
    reason=serializers.CharField()
    startdate=serializers.IntegerField()
    enddate=serializers.IntegerField()
    totaltime =serializers.IntegerField()


    def create(self, validated_data):

        return Goal.objects.create(**validated_data)

    def isDuplicateGoal(self):
        try:

            self.validated_data['user'].goals.get(name=self.validated_data['name'])

            return True

        except:

            return False

class TaskSerializer(serializers.Serializer):

    goalname = serializers.CharField()
    starttime = serializers.IntegerField()
    duration = serializers.IntegerField()

    def create(self, validated_data):

        goal = Goal.objects.get(name=validated_data.pop('goalname'))
        goal.totaltime +=validated_data['duration']
        goal.save(update_fields=["totaltime"])


        return Task.objects.create(**validated_data,goal=goal)