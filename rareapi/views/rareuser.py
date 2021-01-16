from django.http.response import HttpResponseBadRequest
from rest_framework import viewsets
from rest_framework.response import Response
from rareapi.models import RareUser
from rareapi.serializers.rare_user import DetailedRareUserSerializer, RareUserSerializer


class RareUserViewSet(viewsets.ModelViewSet):
    queryset = RareUser.objects.all()
    serializer_class = DetailedRareUserSerializer

    def update(self, request, pk):
      rareuser = self.get_object()
      serializer = RareUserSerializer(rareuser, data=request.data, partial=True)
      if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data)
      else:
          return Response(serializer.errors, status=HttpResponseBadRequest.status_code)

    def get_queryset(self):
      user_id = self.request.query_params.get('user_id', None)
      if user_id:
        return self.queryset.filter(user_id=user_id)
      else:
        return self.queryset