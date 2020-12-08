from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

class RareUser(models.Model):
  bio = models.CharField(max_length=200)
  profile_image_url = models.CharField(max_length=200)
  created_on = models.DateField()
  active = models.BooleanField()
  user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)