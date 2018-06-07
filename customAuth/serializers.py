from rest_framework import serializers
from django.contrib.auth import models, authenticate
from django.utils.translation import ugettext_lazy as _

class signupSerializer(serializers.Serializer):

    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):

        return models.User.objects.create_user(**validated_data)

    def validate_email_isdouble(self):

        try:
            models.User.objects.get(email=self.validated_data['email'])
            return True
        except:
            return False

    def validate_username_isdoublce(self):

        try:
            models.User.objects.get(username=self.validated_data['username'])
            return True
        except:
            return False



class signInSerializer(serializers.Serializer):

    email= serializers.EmailField()
    password =serializers.CharField()

    def athenticate(self):

        username= models.User.objects.get(email= self.validated_data['email']).username
        if username and self.validated_data['password']:

            user =authenticate(username=username,password=self.validated_data['password'])

            if user:
                # From Django 1.10 onwards the `authenticate` call simply
                # returns `None` for is_active=False users.
                # (Assuming the default `ModelBackend` authentication backend.)
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg, code='authorization')
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        return user


class emailSerializer(serializers.Serializer):

    email = serializers.EmailField()

class tokeninfoSerializer(serializers.Serializer):

    username = serializers.CharField()
    token =serializers.CharField()


class responsesigninSerializer(serializers.Serializer):

    result_code= serializers.IntegerField()
    tokeninfo = tokeninfoSerializer()



