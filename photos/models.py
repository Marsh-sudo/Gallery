from unicodedata import category
from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=80)

    def __str__(self):
        return self.location_name

    def save_location(self):
        return self.save()

class Category(models.Model):
    category_name = models.CharField(max_length=60)

    def __str__(self):
        return self.category_name