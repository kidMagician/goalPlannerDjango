from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class signup(APIView):

    def post(self,requst):

        user =signupSerializer(data= requst.data)

        if user.is_valid():
            """
            FAIL_SIGNUP =0;
            SUCEES_SIGNUP =1;
            USERNAM_DUPLICATION= 2;
            EMAIL_NOT_EXIST =3;
            EMAIL_DUPLICATION=4;
            DUPLICATION_USERNAME_EMIL=6;
            """
            if user.validate_email_isdouble() and user.validate_username_isdoublce():
                return  Response({'result':'6'},status = status.HTTP_201_CREATED)
            elif user.validate_email_isdouble():
                return Response({'result': '4'}, status=status.HTTP_201_CREATED)
            elif user.validate_username_isdoublce():
                return Response({'result':'2'},status = status.HTTP_201_CREATED)

            user.save()

            return Response({'result':'1'},status = status.HTTP_201_CREATED)

        else:

            return Response({'result':'0'},status = status.HTTP_400_BAD_REQUEST)


class signin(APIView):

    def post(self,request):

        userS= signInSerializer(data=request.data)

        if userS.is_valid():

            user =userS.athenticate()

            response = responsesigninSerializer(data={'result_code':'1','tokeninfo':{'username':user.username,'token':user.auth_token.key}})

            if response.is_valid():

                return Response(response.data,status=status.HTTP_200_OK)

            else:
                return Response({'result_code': 0}, status=status.HTTP_400_BAD_REQUEST)

        else:

            return Response({'result_code':0},status=status.HTTP_400_BAD_REQUEST)


class findpass(APIView):

    def post(self,request):

        email =emailSerializer(data=request.data)

        if email.is_valid():

            pass

# Create your views here.
