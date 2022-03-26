from unicodedata import category
from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.
class LocationTestClass(TestCase):
    #set up method
    def setUp(self):
        self.new_location = Location(location_name = "Nairobi")

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    #testing save method
    def test_save_method(self):
        self.new_location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_delete_method(self):
        Location.delete_location(self.new_location.id)
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category_name = 'travel')
        self.category.save()


class ImageTestClass(TestCase):

    def setUp(self):
        #creating a new location saving it
        self.London = Location(location_name = 'London')
        self.London.save_location()

        #creating a new category
        self.new_category = Category(category_name = 'travel')
        self.new_category.save_category()

        self.new_image = Image(img_name = 'The mountains',img_desc = 'The mountains of Iceland',location = self.London)
        self.new_image.save()

    #test save method
    def test_save_method(self):
        self.new_image.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)
