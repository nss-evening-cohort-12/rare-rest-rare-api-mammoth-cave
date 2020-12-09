from rest_framework import serializers
from rareapi.models import RareUser

class RareUserSerializer(serializers.ModelSerializer):
  class Meta:
    Model = RareUser
    fields = ('id', 'bio', 'profile_image_url', 'created_on', 'active', 'user_id')
