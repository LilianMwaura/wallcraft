from django.test import TestCase
from .models import *
# Create your tests here.
class LocationTestClass(TestCase):       
      # Set up method
    def setUp(self):
        self.Nairobi= Location(location='Nairobi')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Nairobi,Location))    
        
    def test_save_method(self):
        self.Nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)  
class categoriesTestClass(TestCase):       
      # Set up method
    def setUp(self):
        self.Portrait= categories(category='Portrait')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Portrait,categories))    
        
    def test_save_method(self):
        self.Portrait.save_category()
        categorie = categories.objects.all()
        self.assertTrue(len(categorie)>0)    

