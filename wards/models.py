from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contacts = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'
            