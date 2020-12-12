from rest_framework import serializers
from rareapi.models import Comment, Post

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ('id', 'author_id', 'post_id', 'conent', 'subject', 'created_on')

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('id', 'user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content', 'approved', 'tags')
    depth = 1
