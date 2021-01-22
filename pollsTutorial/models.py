#from django.db import models

# Create your models here.
from djongo import models

class Polls(models.Model):
    _id = models.ObjectIdField()
    post_title = models.CharField(max_length = 255)
    post_description = models.TextField()
    comment = models.JSONField()
    tags = models.JSONField()
    user_details = models.JSONField()
    objects = models.DjongoManager()