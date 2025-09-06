from rest_framework import serializers
from .models import Posts, Comment
from django.contrib.auth import get_user_model

user = get_user_model

class PostSerializer(serializers.Serializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Posts
        fields  = ('author', 'title', 'content', 'created_at', 'updated_at')
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, 'user'):
            validated_data['author'] = request.user
        return super().create(validated_data)

class CommentSerializer(serializers.Serializer):
    author = serializers.ReadOnlyField(source="author.username")
    post = serializers.PrimaryKeyRelatedField(queryset=Posts.objects.all())

    class Meta:
        model = Comment
        fields  = ('author', 'title', 'content', 'created_at', 'updated_at')
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, 'user'):
            validated_data['author'] = request.user
        return super().create(validated_data)