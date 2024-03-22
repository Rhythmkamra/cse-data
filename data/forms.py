from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'rollno', 'year', 'event_type', 'intercollege_mcq', 'intracollege_mcq', 'position', 'is_active']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['event_type'].initial = Student.EVENT_TYPE_DEFAULT
