from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate

class UserRegistrationSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "password", "bio", "profile_picture")

    def create(self, validate_data):
        user = CustomUser.objects.create_user(
            username=validate_data["username"],
            email=validate_data.get["email"],
            password=validate_data.get["password"],
            bio=validate_data.get("bio", ""),
            profile_picture=validate_data.get("profile_picture"),
        )
        return user
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid login details")
        attrs["user"] = user
        return attrs
    
class UserSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "bio", "profile_picture")