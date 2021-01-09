from rest_framework import serializers
from rareapi.models import RareUser
from django.contrib.auth.models import User

class RareUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = RareUser
    fields = ('id', 'bio', 'profile_image_url', 'created_on', 'active', 'user_id')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', "is_staff"]

    
class DetailedRareUserSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)
    class Meta:
        model = RareUser
        fields = ('id', 'bio', 'profile_image_url', 'created_on', 'active', 'user_id')
        depth = 1