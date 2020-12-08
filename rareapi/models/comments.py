from django.db import models
from django.db.models.deletion import CASCADE

class Comment(models.Model):
    author_id = models.ForeignKey("RareUser",
        on_delete=CASCADE,
        related_name="comments",
        related_query_name="comment")
    post_id = models.ForeignKey("Post",
        on_delete=CASCADE,
        related_name="comments",
        related_query_name="comment")
    content = models.TextField()
    subject = models.CharField(max_length=50)
    created_on = models.DateTimeField()