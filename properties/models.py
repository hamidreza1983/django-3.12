from django.db import models
from root.models import Agent

# Create your models here.

class PropertyType(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Status(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Property(models.Model):
    image1 = models.ImageField(upload_to='property/', default='property/default.jpg')
    image2 = models.ImageField(upload_to='property/', default='property/default.jpg')
    image3 = models.ImageField(upload_to='property/', default='property/default.jpg')
    title = models.CharField(max_length=200)
    description = models.TextField()
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING)
    video = models.TextField(blank=True, null=True)
    floor = models.ImageField(upload_to='property/', default='property/default.jpg')
    map = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200)
    type = models.ForeignKey(PropertyType, on_delete=models.DO_NOTHING)
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    area = models.IntegerField(default=0)
    garage = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    position = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']