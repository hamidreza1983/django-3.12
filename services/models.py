from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Specials(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return str(self.text)
    
class Services(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='services/', default='services/default.png')
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=250)
    short_content = models.TextField()
    speacials = models.ManyToManyField(Specials)
    long_content = models.TextField()
    catalog_link = models.URLField(blank=True, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']