from django.db import models

class Skills(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# Create your models here.