from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django import forms

from .models import Profile, Post

from pyuploadcare.dj.forms import ImageField

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        models = 'User'
        fields = ['Username', 'Email', 'Password1', 'Password2']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image' ,'bio', 'contacts']
        
class PostForm(forms.ModelForm):
    photo = ImageField(label='')
    
    class Meta:
        model = Post
        fields = ('photo',)