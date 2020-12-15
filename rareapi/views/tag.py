from rest_framework import viewsets
from rareapi.models import Tag
from rareapi.serializers import TagSerializer

class TagViewSet(viewsets.ModelViewSet):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer
