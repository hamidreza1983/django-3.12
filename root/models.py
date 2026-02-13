from django.db import models

class Skills(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class Agent(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='agents/', default='agents/default.jpg')
    skill = models.ForeignKey(Skills, on_delete=models.DO_NOTHING)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    

class Star(models.Model):
    count = models.IntegerField()

    def __str__(self):
        return str(self.count)
    
class Testimonial(models.Model):
    score = models.ForeignKey(Star, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='testimonials/', default='testimonials/default.jpg')
    position = models.CharField(max_length=100)
    message = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def score_count(self):
        return range(self.score.count)


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.