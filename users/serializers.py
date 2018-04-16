
from rest_framework import serializers
from django.db import transaction
from .models import *


class UserInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password', 'Phone_number', 'first_name', 'last_name', 'national_id')

    def create(self, validated_data):
        created_user = User.objects.create_user(**validated_data)

        return created_user
