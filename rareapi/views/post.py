from rest_framework import viewsets
from rareapi.models import Post
from rareapi.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer