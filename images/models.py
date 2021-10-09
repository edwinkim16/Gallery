from django.db import models
import datetime as dt
from django.db.models import Q

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=100)

    # save location to database
    def save_location(self):
        self.save()

    # update location
    def update_location(self, location):
        self.location = location
        self.save()

     # delete location from database
    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']

class Category(models.Model):
    category = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls,category):
        cls.objects.filter(category=category).delete()

    def __str__(self):
        return self.category        

class Image(models.Model):
    title=models.CharField(max_length=60)
    categories = models.ManyToManyField(Category)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title        