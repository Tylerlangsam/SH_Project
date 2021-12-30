from django.db import models

# Create your models here.

# A model for the Babysitter profiles
class Babysitter(models.Model):
# This model takes 3 inputs, name age and gender
    babysitter_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=20)

# A model for the Child profiles
class Child(models.Model):
# This model takes 4 inputs, name, age, gender, and a many to many field from the Babysitter model
    child_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    age = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    babysitters = models.ManyToManyField(Babysitter)

# A model to create a report
class Report(models.Model):
    # this model takes 4 inputs, meal, potty, nap, and a foreign key from the Child model
    report_id = models.AutoField(primary_key = True)
    meal = models.CharField(max_length = 255)
    potty = models.CharField(max_length=255)
    nap = models.CharField(max_length=255)
    child = models.ForeignKey(Child, on_delete=models.CASCADE, null=True)
    

