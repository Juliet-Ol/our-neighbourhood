from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from .models import Business, Neighbourhood, Profile, Post
from django.contrib.auth.decorators import login_required

from .forms import BusinessForm,  PostForm, ProfileForm

# Create your views here.
@login_required(login_url='login')
def index(request):
    profile_form=ProfileForm
    post_form=PostForm
    post=Post
    if not request.user.profile.neighbourhood:
        post = []
    else:
        currentNeighbourhoodId = request.user.profile.neighbourhood.id
        post=Post.display(currentNeighbourhoodId)
    
    business_form=BusinessForm
    business=Business


    return render(request, 'neighbourhoodwatch/index.html', {"profile_form":profile_form, "post_form":post_form, "posts":post, "business_form":business_form, "business":business})



def register(request):
    form = UserCreationForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
   
            profile = Profile()
            profile.name = form.cleaned_data['username']
            profile.neighbourhood = None
            profile.user = user
            profile.save()

            messages.success(request, 'User has been registered')

            return redirect ('/accounts/login')
        else:
            return render(request, 'registration/registration_form.html', {'form': form})

    else:
        return render(request, 'registration/registration_form.html', {'form': form})


def neighbourhoods(request):
    neighbourhoods = Neighbourhood.objects.all()
    # neighbourhoods = neighbourhoods[len(neighbourhoods)-1]
    context = {
        'neighbourhoods': neighbourhoods,
    }
    print()
    print(neighbourhoods)
    return render(request, 'hoody/hood.html', context)        




def join_neighbourhood(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, pk=id)
    print(request.user)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('/hood')


def leave_neighbourhood(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, pk=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('/hood')
  



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
        
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.post = form.cleaned_data['post']
            post.author = current_user
            post.picture = form.cleaned_data['picture']
            post.neighbourhood = request.user.profile.neighbourhood
            post.save()
            messages.success(request, 'Posted')

            return redirect ('index')
        else:
            return render(request, 'post/new_post.html', {'form': form})

    else:
        return render(request, 'post/new_post.html', {'form': form})    

def editPost(request, id):
    post = get_object_or_404(Post, pk=id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        print(request.POST['post'])
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.post = form.cleaned_data['post']
            post.picture = form.cleaned_data['picture']
            post.save()
            messages.success(request, 'Posted')

            return redirect ('index')
        else:
            return render(request, 'post/edit_post.html', {'form': form, 'postId': post.id})

    else:
        return render(request, 'post/edit_post.html', {'form': form, 'postId': post.id})    

def viewPost(request, id):
    post = get_object_or_404(Post, pk=id)
    

    return render(request, 'neighbourhoodwatch/show.html', {
        'post': post,
       
    }) 





def CreateBusiness(request):
    if request.method=='POST':
        form=BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business=form.save(commit=False)
            business.admin=request.user.profile
            business.save()
            return redirect ('index')
    else:
        form=BusinessForm()
    return render(request,'hoodq.html',{'form':form})








# def business(request):
#     form = BusinessForm
#     current_user = request.user
#     if request.method == 'POST':
       
#         form = BusinessForm(request.POST, request.FILES)
        
#         if form.is_valid():
#             business=form.save(commit=False)
#             business.admin=request.user.profile
#             business = Business()
#             business.business_name = form.cleaned_data['business_name']
#             business.email = form.cleaned_data['email']
#             business.user = current_user
#             business.picture = form.cleaned_data['picture']
#             business.neighbourhood = request.user.profile.neighbourhood
#             business.save()
#             messages.success(request, 'Business registered')

#             return redirect ('index')
#         else:
#             return render(request, 'business/new_business.html', {'form': form})

#     else:
#         return render(request, 'business/new_business.html', {'form': form})    

# def editBusiness(request, id):
#     business = get_object_or_404(Business, pk=id)
#     form = BusinessForm(instance=business)
#     if request.method == 'POST':
        
#         form = BusinessForm(request.POST, request.FILES)
        
#         if form.is_valid():
#             business.business_name = form.cleaned_data['business_name']
#             business.user = form.cleaned_data['user']
#             business.picture = form.cleaned_data['picture']
#             business.save()
#             messages.success(request, 'Business edited')

#             return redirect ('index')
#         else:
#             return render(request, 'business/edit_business.html', {'form': form, 'businessId': business.id})

#     else:
#         return render(request, 'business/edit_business.html', {'form': form, 'businessId': business.id})    


# def viewBusiness(request, id):
#     business = get_object_or_404(Business, pk=id)
    

#     return render(request, 'neighbourhoodwatch/show.html', {
#         'business': business,
       
#     }) 



    



   
            
      
        
      



        

