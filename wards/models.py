from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from pyuploadcare.dj.models import ImageField

class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    live_link=models.CharField(max_length=1000)
    date_posted = models.DateField(default=timezone.now)
    photo = ImageField(blank=True, manual_crop="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Profile(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contacts = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'
    
class Review(models.Model):
    body = models.CharField(max_length=200)
    date_posted = models.DateField(default=timezone.now)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id=models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.body
    
    
    
    
            