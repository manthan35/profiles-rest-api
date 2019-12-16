from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """serializes a name filed for testing out APIViews"""
    name = serializers.CharField(max_length=10)


class UserProfileserializer(serializers.ModelSerializer):
    """serliazes a user profile object""" 

    class Meta:
        model = models.UserProfile
        fields=('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style' : {'input_type':'password'}
            }
        }

    def create(self, validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user