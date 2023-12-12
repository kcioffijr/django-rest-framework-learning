from django.db import models


class MovieData(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    category = models.CharField(max_length=200, default='N/A')
