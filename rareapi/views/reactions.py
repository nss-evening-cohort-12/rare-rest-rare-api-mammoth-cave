from rest_framework import viewsets
from rareapi.models import Reaction
from rareapi.serializers import ReactionSerializer

class ReactionViewSet(viewsets.ModelViewSet):
  queryset = Reaction.objects.all()
  serializer_class = ReactionSerializer
