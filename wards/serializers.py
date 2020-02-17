from rest_framework import serializers
from .models import Post, Profile

class PostSerializers(serializers.ModelSerializer):
    '''
    class that converts post model to json object and viceversa
    '''
    
    class Meta:
        model = Post
        fields = ['title','description', 'live_link', 'photo', 'date_posted', 'author']
        
class ProfileSerializers(serializers.ModelSerializer):
    '''
    class that converts profile model to json object and viceversa
    '''
    class Meta:
        model = Profile
        fields = ['image','user', 'contacts', 'bio']