from django import forms
from .models import Post, Profile, Neighbourhood

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude =['user', 'id']
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'published_date']
        fields = '__all__'       