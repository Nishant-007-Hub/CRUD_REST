from django.db import models
from django.db.models.deletion import CASCADE


class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=CASCADE, related_name='sung_by')
    duration = models.IntegerField(default=0)

    def __str__(self):
        return self.title
