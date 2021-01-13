from rest_framework import viewsets, parsers
from rareapi.models import Image
from rareapi.serializers import ImageSerializer

class ImageViewSet(viewsets.ModelViewSet):
  parser_classes = [parsers.MultiPartParser]  
  queryset = Image.objects.all()
  serializer_class = ImageSerializer
