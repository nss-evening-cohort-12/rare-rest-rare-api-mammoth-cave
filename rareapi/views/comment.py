from django.http.response import HttpResponseBadRequest
from rest_framework import viewsets
from rest_framework.response import Response
from rareapi.models import Comment
from rareapi.serializers.comment import CommentCreateSerializer, CommentUpdateSerializer, CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request):
      serializer = CommentCreateSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data)
      else:
          return Response(serializer.errors, status=HttpResponseBadRequest.status_code)
    
    
    def update(self, request, pk):
      post = self.get_object()
      serializer = CommentUpdateSerializer(post, data=request.data, partial=False)
      if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data)
      else:
          return Response(serializer.errors, status=HttpResponseBadRequest.status_code)

    def get_queryset(self):
      user_id = self.request.query_params.get('user_id', None)
      post_id = self.request.query_params.get('post_id', None)
      if user_id:
        return self.queryset.filter(user_id=user_id)
      elif post_id:
        return self.queryset.filter(post_id=post_id)
      else:
        return self.queryset
