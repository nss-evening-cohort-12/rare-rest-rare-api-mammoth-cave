from rest_framework import serializers
from rareapi.models import PostReaction, Reaction

class ReactionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reaction
    fields = ('id', 'label', "img_url")

class PostReactionSerializer(serializers.ModelSerializer):
  reaction_id = ReactionSerializer(read_only=True)
  class Meta:    
    model = PostReaction
    fields = ('id', 'user_id', 'post_id', 'reaction_id')

class PostPostReactionSerializer(serializers.ModelSerializer):
  class Meta:
    model= PostReaction
    fields = ('id', 'user_id', 'post_id', 'reaction_id')