# Create a ModelForms
from django import forms

from student.models import Student

class student_forms(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__" # Specify that the all model field from the student_forms should be included.

# Here student_forms is the class which inherits the ModelForm class properties and the class meta is the decorator for the class.
# models = student means we want our form to have the models of the student class and fields = "__all__" 
# we should use all fields from student class.
# Then what does the ModelForm and model = Student and this fields = __all__ means?? ,  
# There is one interesting thing about django that it actually helps us by creating a form for our model.




    
