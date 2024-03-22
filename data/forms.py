# forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'rollno', 'year', 'event_type', 'intercollege_mcq', 'intracollege_mcq', 'position']
