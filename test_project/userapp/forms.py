from django import forms
from .models import Student
from django.db.models import Q

class StudentForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(StudentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Student
        fields = ["name", "dob","gender"]    