from rest_framework import viewsets
from rareapi.models import PostReaction
from rareapi.serializers import PostReactionSerializer

class PostReactionViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Subscription.
    """
    queryset = PostReaction.objects.all()
    serializer_class = PostReactionSerializer


    def get_queryset(self):
        post_id = self.request.query_params.get('post_id', None)
        reaction_id = self.request.query_params.get('reaction_id', None)
        if reaction_id and post_id:
            return self.queryset.filter(post_id=post_id).filter(reaction_id=reaction_id)
        if post_id:
            return self.queryset.filter(post_id=post_id)
        else:
            return self.queryset