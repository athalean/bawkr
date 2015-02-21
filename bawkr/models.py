from django.db import models


class Bawk(models.Model):
    class Meta:
        ordering = ['-posted_on']

    username = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    posted_on = models.DateTimeField(auto_now_add=True)