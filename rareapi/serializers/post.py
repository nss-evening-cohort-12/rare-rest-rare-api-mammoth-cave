from rest_framework import serializers
from rareapi.models import Post, RareUser, Category
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'label']
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
    user_id = RareUserSerializer(read_only=True)
    category_id = CategorySerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content', 'approved', 'tags')

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content', 'approved', 'tags')

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content', 'approved', 'tags')