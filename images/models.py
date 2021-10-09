from django.db import models

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