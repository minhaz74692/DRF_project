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
    
    #De-Serialization
    def update(self, instance, validated_data):
        instance.user_name = validated_data.get("user_name", instance.user_name)
        instance.age = validated_data.get("age", instance.age)
        instance.profession = validated_data.get("profession", instance.profession)
        instance.save()
        return instance