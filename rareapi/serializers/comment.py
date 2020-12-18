from rest_framework import serializers
from rareapi.models import Comment, Post, RareUser 
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ('id', 'author_id', 'post_id', 'content', 'subject', 'created_on')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

class RareUserSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)
    class Meta:
        model = RareUser
        fields = ('id', 'user_id')
        depth = 1

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('id', 'user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content', 'approved', 'tags')
    depth = 1

class CommentCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ('id', 'author_id', 'post_id', 'content', 'subject', 'created_on')

class CommentUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ('id', 'author_id', 'post_id', 'content', 'subject', 'created_on')