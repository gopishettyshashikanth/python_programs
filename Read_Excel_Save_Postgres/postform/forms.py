from django import forms
from .models import fileupload

class userForm(forms.ModelForm):
	
	class Meta:
		model = fileupload
		fields = ('file',)
