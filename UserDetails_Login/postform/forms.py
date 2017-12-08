from django import forms
from .models import UserCategory,User

from django.db import models
from django.forms import ModelForm


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)         

class userForm(forms.ModelForm):
	
	#photos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

	gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
	
	class Meta:
		model = UserCategory
		fields = ('name','Email','salary','gender','phone_number','state','status','photoID','deptID',)

class signupForm(forms.Form):

	class Mata:
		model = User
		fields = ('location')