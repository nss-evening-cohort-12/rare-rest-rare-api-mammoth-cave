from django.db import models
from django.db.models.deletion import CASCADE

class PostReaction(models.Model):

    user_id = models.ForeignKey("RareUser",
        on_delete=CASCADE,
        related_name="users",
        related_query_name="user")
    reaction_id = models.ForeignKey("Reaction",
        on_delete=CASCADE,
        related_name="reactions",
        related_query_name="reaction")
    post_id = models.ForeignKey("Post",
        on_delete=CASCADE,
        related_name="posts",
        related_query_name="post")