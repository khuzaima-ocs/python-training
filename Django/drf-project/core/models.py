from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    dob = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
    
