from django.db import models

# Create your models here.

GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others','Others')
    )

class Student(models.Model):
	name = models.CharField(max_length=50,blank=True,null=True)
	gender = models.CharField(choices=GENDER_CHOICES,max_length=100,blank=True,null=True)
	dob = models.DateField(max_length=50,blank=True,null=True)