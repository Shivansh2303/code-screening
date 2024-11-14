# serializers.py
from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class CommentDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username') 

    class Meta:
        model = Comment
        fields = ['text', 'timestamp', 'user']

class PostListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')  
    comments = serializers.SerializerMethodField()
    comment_count = serializers.IntegerField(source='comments.count', read_only=True) 

    class Meta:
        model = Post
        fields = ['text', 'timestamp', 'user', 'comment_count', 'comments']

    def get_comments(self, obj):
        comments = obj.comments.order_by('-timestamp')[:3]
        return CommentDetailSerializer(comments, many=True).data
