from django import forms
from .models import UserCategory

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)         

class userForm(forms.ModelForm):
	
	gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
	class Meta:
		model = UserCategory
		fields = ('name','Email','salary','gender','state','status')
		
        


		




