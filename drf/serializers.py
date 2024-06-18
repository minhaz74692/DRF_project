from rest_framework import serializers
from . models import User

class UserSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=25)
    user_id = serializers.CharField(max_length=20)
    age = serializers.IntegerField()
    profession = serializers.CharField(max_length=25)

    #De-Serialization
    def create(self, validated_data):
        return User.objects.create(**validated_data)