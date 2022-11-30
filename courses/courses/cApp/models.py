from django.db import models

# Create your models here.

class Courses(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.description} {self.rating}"