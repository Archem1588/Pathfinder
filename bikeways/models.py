from django.db import models
from xml.etree.ElementTree import ElementTree

# Create your models here.


class CoordinateData(models.Model):
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)





