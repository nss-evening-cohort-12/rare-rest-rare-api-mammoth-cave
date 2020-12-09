from rest_framework import serializers
from rareapi.models import Comment

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    Model = Comment
    fields = ('id', 'author_id', 'post_id', 'conent', 'subject', 'created_on')
