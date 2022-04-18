from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

import neighbourhoodwatch
from .models import Business, Neighbourhood, Profile, Post
from django.contrib.auth.decorators import login_required

from .forms import BusinessForm, NeighbourhoodForm, PostForm, ProfileForm

# Create your views here.

def index(request):
    profile_form=ProfileForm
    post_form=PostForm
    post=Post
    post=Post.display()
    business_form=BusinessForm
    business=Business


    return render(request, 'neighbourhoodwatch/index.html', {"profile_form":profile_form, "post_form":post_form, "posts":post, "business_form":business_form, "business":business})



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


  



def editProfile(request):
    profile=Profile.objects.get(user= request.user.id)

    form = ProfileForm(initial={'name':profile.name, 'bio':profile.bio, 'email':profile.email})

   
    return render(request, 'profile/edit.html', {'form': form})  


def profile(request):
    form = ProfileForm

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        # Profile.objects.filter(id__gt=1)
        
        profile=Profile.objects.get(user= request.user.id)
       
        if form.is_valid():

            

            profile.image=form.cleaned_data['image'] if len(request.FILES) != 0 else profile.image
            profile.name=form.cleaned_data['name']  
            profile.bio=form.cleaned_data['bio'] 
            profile.email=form.cleaned_data['email'] 

           
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
        


def post(request):
    form = PostForm
    current_user = request.user
    if request.method == 'POST':
        print(request.POST['post'])
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.post = form.cleaned_data['post']
            post.author = current_user
            post.picture = form.cleaned_data['picture']
            post.save()
            messages.success(request, 'Posted')

            return redirect ('index')
        else:
            return render(request, 'post/new_post.html', {'form': form})

    else:
        return render(request, 'post/new_post.html', {'form': form})    


def viewPost(request, id):
    post = get_object_or_404(Post, pk=id)
    

    return render(request, 'neighbourhoodwatch/show.html', {
        'post': post,
       
    }) 









   
            
      
        
      



        

