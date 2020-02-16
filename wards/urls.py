from django.urls import path
from . import views
from .views import PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', views.home, name='wards-home'),
    
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]

