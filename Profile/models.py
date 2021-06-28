from django.db import models

# Create your models here.

class Tutorials(models.Model):
    email = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)

class Exam(models.Model):
    email = models.CharField(max_length=100)
    ecode = models.CharField(max_length=100)
    questions = models.CharField(max_length=1000)
    options_a = models.CharField(max_length=100)
    options_b = models.CharField(max_length=100)
    options_c = models.CharField(max_length=100)
    options_d = models.CharField(max_length=100)
    answers = models.CharField(max_length=100)