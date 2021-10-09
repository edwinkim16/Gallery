from django.test import TestCase
from .models import Location,Category,Image
import datetime as dt

# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.Moringa = Location(location='London')

    def test_instance(self):
        self.assertTrue(isinstance(self.Moringa,Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_method(self):
        self.Moringa.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        self.Moringa.delete_location('London')
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.Food = Category(category='Football')

    def test_instance(self):
        self.assertTrue(isinstance(self.Food,Category))

    def tearDown(self):
        Category.objects.all().delete()

    def test_save_method(self):
        self.Food.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_method(self):
        self.Food.delete_category('Football')
        category = Category.objects.all()
        self.assertTrue(len(category)==0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.test_category = Category(category=list('Football'))
        self.test_category.save_category()

        self.location = Location(location="London")
        self.location.save_location()

        self.image = Image(id=1,title="Football",categories=self.test_category,location=self.location,)
        self.image.save_image()

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_save_image(self):
        images = Image.objects.all()
        self.assertTrue(len(images)>0)