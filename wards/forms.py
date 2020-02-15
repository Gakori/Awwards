from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django import forms

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        models = 'User'
        fields = ['Username', 'Email', 'Password1', 'Password2']