from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm

# Create your views here.

def index(request):
    profile_form=ProfileForm


    return render(request, 'neighbourhoodwatch/index.html', {"profile_form":profile_form})



def register(request):
    form = UserCreationForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been registered')

            return redirect ('/accounts/login')
        else:
            return render(request, 'registration/registration_form.html', {'form': form})

    else:
        return render(request, 'registration/registration_form.html', {'form': form})
        
@login_required(login_url='login')
def editProfile(request):
    profile=Profile.objects.get(user= request.user.id)

    form = ProfileForm(initial={'name':profile.name, 'bio':profile.bio, 'email':profile.email})

   
    return render(request, 'profile/edit.html', {'form': form})  


def profile(request):
    form = ProfileForm

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
             
        profile=Profile.objects.get(user= request.user.id)
       
        if form.is_valid():

          
            profile.image=form.cleaned_data['image'] if len(request.FILES) != 0 else profile.image
            profile.name=form.cleaned_data['name']  
            # profile.id= form.cleaned_data['id']            
            profile.email=form.cleaned_data['email'] 
            profile.bio=form.cleaned_data['bio']             
            profile.save()

           
            messages.success(request, 'Profile has been updated')

            return redirect ('/profile')
        else:
            return render(request, 'profile/edit.html', {'form': form})

    else:
        

        if Profile.objects.filter(user = request.user.id).count() == 0:
            profile = Profile(user=request.user, name=request.user.username, email=request.user.email, bio='')
            profile.save()
        else:
            profile= request.user.profile 
        return render(request, 'profile/profile.html', {'form': form, 'profile':profile})    