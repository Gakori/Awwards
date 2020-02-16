from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm, PostForm

from django.http import HttpResponse

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from django.views.generic import ListView , CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post

from django.urls import reverse_lazy

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = PostForm()

    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        posts = None
    
    return render(request, 'wards/home.html', { 'posts': posts, 'form': form })

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description']
    success_url = reverse_lazy('wards-home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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
        
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'wards/profile.html', context)
        
