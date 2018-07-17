from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,authentication_classes
from django.views.decorators.csrf import csrf_exempt


class goal(APIView):

    authentication_classes = (TokenAuthentication,)

    def get(self,request):

        goals =request.user.goals

        serializers = GoalSerializer(goals,many=True)

        return Response({'results':serializers.data},status=status.HTTP_200_OK)

    def post(self,request):

        goalS = GoalSerializer(data=request.data)

        if goalS.is_valid():

            goalS.validated_data['user'] = request.user

            if goalS.isDuplicateGoal():

                return Response({'result_code':'2'}, status=status.HTTP_201_CREATED)

            goalS.save()

            return Response({'result_code':'1'}, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):

        goalS = GoalSerializer(data=request.data)

        if goalS.is_valid():

            goalS.delete()

        pass

    def put(self,requst):


        pass

class task(APIView):

    def post(self,request):

        task  = TaskSerializer(data=request.data)

        if task.is_valid():

            task.save()

            return Response({'result_code': '1'}, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)






# Create your views here.
