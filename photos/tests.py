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
