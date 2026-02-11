from rest_framework import serializers
from .models import User, Run

class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ['id', 'user', 'distance_meters', 'duration_seconds', 'start_time']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']