from django.db import models
from django.db.models.deletion import CASCADE

class Post(models.Model):
    user_id = models.ForeignKey("RareUser",
        on_delete=CASCADE,
        related_name="posts",
        related_query_name="post")
    category_id = models.ForeignKey("Category",
        on_delete=CASCADE,
        related_name="posts",
        related_query_name="post")
    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    image_url = models.CharField(max_length=200)
    content = models.TextField()
    approved = models.BooleanField()
    tags = models.ManyToManyField(
        "Tag",
        related_name="posts",
        related_query_name="post"
    )