from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# from neighbourhoodwatch.views import neighbourhood
from .models import Business, Post, Profile, Neighbourhood

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude =['user', 'identity_number']
        fields = '__all__'

            


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'published_date']
        fields = '__all__'       

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        
        fields = '__all__'               