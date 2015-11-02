from django.db import models
from xml.etree.ElementTree import ElementTree

# Create your models here.


class CoordinateData(models.Model):
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    #
    # @classmethod
    # def create(cls, lat, lng):
    #     c = cls(latitude=lat, longitude=lng)
    #     return c

    # Return latitude for now
    def __str__(self):
        return self.lat



