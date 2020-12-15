from django.http.response import HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework import viewsets
from rareapi.models import Post
from rareapi.serializers import PostSerializer, PostCreateSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request):
      serializer = PostCreateSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data)
      else:
          return Response(serializer.errors, status=HttpResponseBadRequest.status_code)