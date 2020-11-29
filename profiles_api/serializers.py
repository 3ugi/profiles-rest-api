# 33. Create a Serializer
from rest_framework import serializers

# 45. Create user profile serializer
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """ Serializers a name field for testing our APIView. """

    name = serializers.CharField(max_length=10)
    # surname = serializers.CharField(max_length=10)


# 45. Create user profile serializer
class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object. """

    # Use metaclass to configure serializer to point to specific module in the project
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """ Create and return a new user. """
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
