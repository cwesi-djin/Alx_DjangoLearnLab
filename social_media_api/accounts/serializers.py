from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token

user = get_user_model


class UserRegistrationSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "password", "bio", "profile_picture")

    def create(self, validate_data):
        user = get_user_model().objects.create_user(
            username=validate_data["username"],
            email=validate_data.get["email"],
            password=validate_data.get["password"],
            bio=validate_data.get("bio", ""),
            profile_picture=validate_data.get("profile_picture"),
        )
        Token.objects.create(user=user)
        return user
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):

        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise serializers.ValidationError("Invalid Credentials")
            data["user"] = user

            return data
    
        else:
            raise serializers.ValidationError("Missing field.")

    
class UserSerializer(serializers.Serializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "bio", "profile_picture", 'followers_count', 'following_count')

    def get_followers_count(self, obj):
        return obj.followers.count()
    
    def get_following_count(self, obj):
        return obj.following.count()