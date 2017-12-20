from django import forms
from .models import UserCategory,User

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)         

class userForm(forms.ModelForm):
	
	#photos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
	gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
	phone_number = forms.RegexField(regex=r'^[0-9]{10}$', max_length=10,
                                error_message = ("Phone number must be entered in the format: '9999999999'. Up to 10 digits allowed."))

	class Meta:
		model = UserCategory
		fields = ('name','Email','salary','gender','phone_number','state','status','photoID','deptID',)

class signupForm(AbstractUser):

	class Mata:
		model = User
		fields = ('location')