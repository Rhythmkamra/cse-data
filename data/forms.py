from django import forms
from .models import Student_cultural, Student_sports, Student_technical

class StudentFormCultural(forms.ModelForm):
    class Meta:
        model = Student_cultural
        fields = ['name', 'rollno', 'year', 'event_name', 'event_description', 'event_type', 'intercollege_mcq', 'intracollege_mcq', 'position', 'is_active']

    def __init__(self, *args, **kwargs):
        super(StudentFormCultural, self).__init__(*args, **kwargs)
        self.fields['event_type'].initial = Student_cultural.EVENT_TYPE_DEFAULT
        self.fields['name'].initial = 'Default Name'
        self.fields['event_description'].initial = 'Default Description'


class StudentFormSports(forms.ModelForm):
    class Meta:
        model = Student_sports
        fields = ['name', 'rollno', 'year', 'event_name', 'event_description', 'event_type', 'intercollege_mcq', 'intracollege_mcq', 'position', 'is_active']

    def __init__(self, *args, **kwargs):
        super(StudentFormSports, self).__init__(*args, **kwargs)
        self.fields['event_type'].initial = Student_sports.EVENT_TYPE_DEFAULT
        self.fields['name'].initial = 'Default Name'
        self.fields['event_description'].initial = 'Default Description'


class StudentFormTechnical(forms.ModelForm):
    class Meta:
        model = Student_technical
        fields = ['name', 'rollno', 'year', 'event_name', 'event_description', 'event_type', 'intercollege_mcq', 'intracollege_mcq', 'position', 'is_active']

    def __init__(self, *args, **kwargs):
        super(StudentFormTechnical, self).__init__(*args, **kwargs)
        self.fields['event_type'].initial = Student_technical.EVENT_TYPE_DEFAULT
        self.fields['name'].initial = 'Default Name'
        self.fields['event_description'].initial = 'Default Description'
