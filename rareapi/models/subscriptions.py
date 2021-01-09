from django.db import models
from django.db.models.deletion import CASCADE

class Subscription(models.Model):
    follower_id =  models.ForeignKey("RareUser",
        on_delete=CASCADE,
        related_name="followers",
        related_query_name="follower")
    author_id = models.ForeignKey("RareUser",
        on_delete=CASCADE,
        related_name="authors",
        related_query_name="author")