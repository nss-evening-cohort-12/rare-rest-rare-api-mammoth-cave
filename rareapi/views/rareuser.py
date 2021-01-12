from django.http.response import HttpResponseBadRequest
from rest_framework import viewsets
from rest_framework.response import Response
from rareapi.models import RareUser
from rareapi.serializers.rare_user import DetailedRareUserSerializer


class RareUserViewSet(viewsets.ModelViewSet):
    queryset = RareUser.objects.all()
    serializer_class = DetailedRareUserSerializer

    def get_queryset(self):
      user_id = self.request.query_params.get('user_id', None)
      if user_id:
        return self.queryset.filter(user_id=user_id)
      else:
        return self.queryset