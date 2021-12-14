from django.db import models

# Create your models here.

class Babysitter(models.Model):
    babysitter_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=20)

class Child(models.Model):
    child_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    age = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    babysitters = models.ManyToManyField(Babysitter)

class Report(models.Model):
    report_id = models.AutoField(primary_key = True)
    meal = models.CharField(max_length = 255)
    potty = models.CharField(max_length=255)
    nap = models.CharField(max_length=255)
    child_id = models.ForeignKey(Child, on_delete=models.CASCADE)

