from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget= forms.PasswordInput)
    password2 = forms.CharField(widget = forms.PasswordInput , label='Confirm Password')
    
    class Meta:
        model = User
        fields = ['username','email','password','is_teacher','is_student']

        def cleaned_data(self):
            cd = self.cleaned_data
            if cd['password1'] != cd['password2']:
                raise forms.ValidationError('Passeord didnt match !!!')
            else:
                return cd['password2']



