

# Create your models here.
from django.db import models

class Monitor(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    mall_name = models.CharField(max_length=50)
    image_url = models.URLField(blank=True, null=True)
    link = models.URLField()

    def __str__(self):
        return self.title

class Mouse(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    mall_name = models.CharField(max_length=50)
    image_url = models.URLField(blank=True, null=True)
    link = models.URLField()

    def __str__(self):
        return self.title

class Keyboard(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    mall_name = models.CharField(max_length=50)
    image_url = models.URLField(blank=True, null=True)
    link = models.URLField()

    def __str__(self):
        return self.title
