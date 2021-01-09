from rest_framework import viewsets
from rareapi.models import Subscription
from rareapi.serializers import SubscriptionSerializer
import json

class SubscriptionViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Subscription.
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        idsraw = self.request.query_params.get('ids', None)
        if idsraw:
            ids = json.loads(idsraw)
            return self.queryset.filter(follower_id=ids["follower_id"]).filter(author_id=ids["author_id"])
        else:
            return self.queryset