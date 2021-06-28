from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=101)
    phone = models.CharField(max_length=10,unique=True)
    email = models.CharField(max_length=100,unique=True)
    wyd = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    accnttype = models.CharField(max_length=100)
    password = models.CharField(max_length=100)







