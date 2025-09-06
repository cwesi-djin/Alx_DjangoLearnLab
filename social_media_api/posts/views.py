from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from .models import Post, Comment
from rest_framework.pagination import PageNumberPagination

user = get_user_model

class SmallResultsSetPagination(PageNumberPagination):
    page_size = 5  # override page size here
    page_size_query_param = 'page_size'
    max_page_size = 50

# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = SmallResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = SmallResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

