from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']

class Category(models.Model):
    category = models.CharField(max_length=30)

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