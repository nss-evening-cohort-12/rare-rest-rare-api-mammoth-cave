from rest_framework import viewsets
from rareapi.models import RareUser
from rareapi.serializers import RareUserSerializer, DetailedRareUserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = RareUser.objects.all()


    def get_serializer_class(self):
        if self.action == 'list':
            return RareUserSerializer
        if self.action == 'retrieve':
            return DetailedRareUserSerializer
        return serializers.Default