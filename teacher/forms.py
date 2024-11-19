from django import forms
from django.forms import ModelForm
from teacher.models import Teacher 

class Teacher_forms(ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"

# Here the class meta is the decorator , model  = Teacher means the database model needs to be of Teacher and field = __all__ 
# means there should be all fields in the model.

