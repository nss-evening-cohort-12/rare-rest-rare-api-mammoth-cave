from rest_framework import serializers
from rareapi.models import Category

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    Model = Category
    fields = ('id', 'label')
