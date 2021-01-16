from rest_framework import viewsets
from rareapi.models import RareUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from rareapi.serializers import RareUserSerializer, DetailedRareUserSerializer, UserSerializer
from rareapi.serializers.rare_user import RareUserUpdateSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def update(self, request, pk):
      post = self.get_object()
      serializer = UserSerializer(post, data=request.data, partial=True)
      if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data)
      else:
          return Response(serializer.errors, status=HttpResponseBadRequest.status_code)


    def get_serializer_class(self):
        if self.action == 'list':
            return RareUserSerializer
        if self.action == 'retrieve':
            return DetailedRareUserSerializer
        return serializers.Default
