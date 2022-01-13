from django.db import models
from django.db.models.fields import PositiveIntegerField

# Create your models here.

class Patient(models.Model):
    fName = models.TextField()
    mName = models.TextField()
    age = models.PositiveIntegerField()
    lName = models.TextField()
    bDate = models.DateTimeField()
    phone = models.PositiveIntegerField()
    email = models.TextField()
    sex = models.TextField()
    bloodType = models.TextField()



    