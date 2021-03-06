from distutils.command.upload import upload
from email.policy import default
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

    @classmethod
    def delete_location(cls,id):
        return cls.objects.filter(id = id).delete()

class Category(models.Model):
    category_name = models.CharField(max_length=60)

    def __str__(self):
        return self.category_name

    def save_category(self):
        return self.save()


class Image(models.Model):
    img_name = models.CharField(max_length=60)
    img_desc = models.CharField(max_length=60)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'photo/', default = 'no-image')
    

    def __str__(self):
        return self.img_name

    @classmethod
    def show_all_images(cls):
        return cls.objects.order_by("pub_date")

    def save_image(self):
        return self.save()
    
    @classmethod
    def delete_image(cls,id):
        return cls.objects.filter(id = id).delete()

    @classmethod
    def get_image_by_id(cls,id):
        return cls.objects.filter(id = id).all()

    @classmethod
    def search_image_by_category(cls,search_term):
        album = cls.objects.filter(category_category_name__icontains = search_term)
        return album
