from rest_framework import serializers
from . import  models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile  # Replace with your actual model
        fields = ['id', 'name', 'email', 'password']  # Add additional fields here
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'style' : {'input_type' : 'password'}
            }
        }
        def create(self, validated_data):
            user = models.UserProfile.objects.create_user(
                name = validated_data['name'],
                email = validated_data['email'],
                password = validated_data['password']
            )
            return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileFeedItem
        fields = ['id', 'user_profile', 'status_text', 'created_on']
        extra_kwargs = {'user_profile': {'read_only' : True}}
