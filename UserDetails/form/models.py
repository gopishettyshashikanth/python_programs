from django.db import models
from django import forms

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

STATE_CHOICES = (
    ('Telangana', 'TG'),
    ('Andhra Pradesh', 'AP'),
    ('Madhra Pradesh', 'MP')
)

# Create your models here.
class UserCategory(models.Model):
    name = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    salary = models.CharField(max_length=20)
    tds = models.CharField(max_length=20)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    gender = models.CharField(max_length=10,
                              choices=GENDER_CHOICES)
    state = models.CharField(max_length=50,
                              choices=STATE_CHOICES)

    def __str__(self):
    	return "%s"%self.name
    





