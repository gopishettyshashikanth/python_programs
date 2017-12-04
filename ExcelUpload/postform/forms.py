from django import forms
from .models import userDetails

class userForm(forms.ModelForm):
	
	class Meta:
		model = userDetails
		fields = ('file',)
