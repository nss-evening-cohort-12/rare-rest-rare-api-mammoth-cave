from rest_framework import serializers
from rareapi.models import Comment

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ('id', 'author_id', 'post_id', 'content', 'subject', 'created_on')
