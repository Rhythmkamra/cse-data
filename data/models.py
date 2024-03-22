from django.db import models

class Student(models.Model):
    YEAR_CHOICES = (
        (1, 'First Year'),
        (2, 'Second Year'),
        (3, 'Third Year'),
        (4, 'Fourth Year'),
    )
    
    EVENT_TYPE_CHOICES = (
        ('national', 'National'),
        ('state', 'State'),
        ('district', 'District'),
    )
    
    POSITION_CHOICES = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('none', 'None'),
    )
    
    EVENT_TYPE_DEFAULT = 'cultural'  # Default value for event_type

    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=20)
    year = models.IntegerField(choices=YEAR_CHOICES)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES, default=EVENT_TYPE_DEFAULT)
    intercollege_mcq = models.BooleanField(default=False)
    intracollege_mcq = models.BooleanField(default=False)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    is_active = models.BooleanField(default=True)  # Default field
    def __str__(self):
        return self.name