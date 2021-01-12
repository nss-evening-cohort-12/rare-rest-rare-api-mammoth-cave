from django.http.response import HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework import viewsets
from rareapi.models import Post, Subscription
from rareapi.serializers import PostSerializer, PostCreateSerializer, PostUpdateSerializer


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
    
    
    def update(self, request, pk):
      post = self.get_object()
      serializer = PostUpdateSerializer(post, data=request.data, partial=True)
      if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data)
      else:
          return Response(serializer.errors, status=HttpResponseBadRequest.status_code)


    def get_queryset(self):
      user_id = self.request.query_params.get('user_id', None)
      category_id = self.request.query_params.get('category_id', None)
      approved = self.request.query_params.get('approved', None)
      follower = self.request.query_params.get('subscribed', None)
      if user_id:
        return self.queryset.filter(user_id=user_id)
      elif category_id:
        return self.queryset.filter(category_id=category_id)
      elif approved:
        approved = self.queryset.filter(approved=True)
        return self.queryset.filter(approved=True)
      elif follower:
        subscriptions = Subscription.objects.filter(follower_id=follower)
        return self.queryset.filter(user_id__in=subscriptions.values("author_id")).filter(approved=True)
      else:
        return self.queryset