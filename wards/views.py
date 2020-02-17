from django.shortcuts import render, redirect

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PostForm

from django.http import HttpResponse

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Review, Profile

from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from . serializers import PostSerializers

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

class PostList(APIView):
    def get(self, request):
        post1 = Post.objects.all()
        serializer = PostSerializers(post1, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass
    
class ProfileList(APIView):
    def get(self, request):
        profile1 = Profile.objects.all()
        serializer = ProfileSerializers(profile1, many=True)
        return Response(serializer.data)
        
    def post(self):
        pass

# @login_required
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'author', 'description', 'live_link', 'photo']
    success_url = reverse_lazy('wards-home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDetailView(DetailView):
    model = Post
    success_url = reverse_lazy('wards-home')
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title']
    success_url = reverse_lazy('wards-home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})
        
@login_required
def profile(request):
    '''
    function that displays current user
    '''
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

def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
    else:
        form = ReviewForm()

    try:
        reviews = Review.objects.all()
    except Review.DoesNotExist:
        reviews = None
        
    return render(request, 'wards/review.html', { 'reviews': reviews, 'form': form })
    
    