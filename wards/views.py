from django.shortcuts import render, redirect

from .forms import UserRegistrationForm

from django.http import HttpResponse

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

def home(request):
    return HttpResponse('<h2>oiuytr</h2>')

def register(request):
    '''
    function that renders the renders the registration form
    '''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has  been created.You are now able to login')#flash message
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})
        
