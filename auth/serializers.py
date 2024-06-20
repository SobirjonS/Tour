from rest_framework import serializers
from main import models

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'avatar']