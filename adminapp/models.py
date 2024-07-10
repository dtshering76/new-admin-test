from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    length = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"