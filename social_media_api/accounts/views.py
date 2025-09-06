from django.shortcuts import render
from rest_framework import generics, status
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer
from .models import CustomUser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404




# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "user": UserSerializer(user).data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_201_CREATED,
        )
    

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        token, _ = Token.objects.get_or_create(user=user)
        user_data = UserSerializer(user).data

        return Response(
            {
                'token':token.key,
                "user": UserSerializer(user).data,
            },
            status=status.HTTP_200_OK,
        )
    

class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def follow(self, request, pk=None):
        """Authenticated user follows another user"""
        user_to_follow = get_object_or_404(CustomUser, pk=pk)

        if user_to_follow == request.user:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        request.user.following.add(user_to_follow)
        return Response(
            {"detail": f"You are now following {user_to_follow.username}."},
            status=status.HTTP_200_OK,
        )

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def unfollow(self, request, pk=None):
        """Authenticated user unfollows another user"""
        user_to_unfollow = get_object_or_404(CustomUser, pk=pk)

        if user_to_unfollow == request.user:
            return Response(
                {"detail": "You cannot unfollow yourself."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        request.user.following.remove(user_to_unfollow)
        return Response(
            {"detail": f"You have unfollowed {user_to_unfollow.username}."},
            status=status.HTTP_200_OK,
        )

