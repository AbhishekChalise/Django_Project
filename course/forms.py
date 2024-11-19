from django import forms
from course.models import Course

class course_forms(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        




