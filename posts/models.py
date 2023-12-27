from django.db import models

class Post(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=255)
    text = models.TextField()
