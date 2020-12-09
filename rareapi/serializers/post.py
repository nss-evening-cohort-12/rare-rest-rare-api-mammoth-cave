from rest_framework import serializers
from rareapi.models import Post

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    Model = Post
    fields = ('id', 'user_id', 'category_id', 'title', 'publication_date', 'image_url', 'content', 'approved', 'tags')
