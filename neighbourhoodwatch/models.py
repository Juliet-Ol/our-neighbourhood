
# from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Neighbourhood(models.Model):
    name= models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=100, blank=False)
    description =models.TextField(blank=False, null=True)
    housenumber =models.CharField(max_length=100, blank=False)
    admin = models.ForeignKey('Profile',
        on_delete=models.CASCADE,
        related_name='neighbour',
        null='True',
        blank=True,
        default='')
    police = models.IntegerField(blank=True)
    hospital = models.IntegerField(blank=True) 

    def __str__(self):
        return f'{self.name}.neighbourhood' 

    def create_neighborhood(self):
        self.save()
    def delete_neighborhood(self):
        self.delete()
    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)   
        
         
        



class Profile(models.Model):
    name =models.CharField(max_length=50, blank=True)  
    identiy_number = models.CharField(max_length=50, blank=True, primary_key=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete = models.SET_NULL, null=True, blank=True)
    email = models.EmailField(null=True) 
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=300, default='') 

    def __str__(self):
        return f'{self.user.username} Profile'  

    # def __str__(self):
    #     return f'{self.user.neighbourhood} Profile'    

class Post (models.Model):
    title = models.CharField(max_length=20)
    picture = CloudinaryField('image')
    post = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete = models.SET_NULL, null=True, blank=True)
    

    class Meta:
        ordering = ['-published_date']  

    @classmethod
    def display(cls, currentNeighbourhoodId):
        posts = cls.objects.filter(neighbourhood__id = currentNeighbourhoodId).all()
        return posts

    def save_posts(self):
        self.user
    def delete_posts(self):
        self.delete()
    @classmethod
    def search_posts(cls, name):
        return cls.objects.filter(title__icontains=name).all() 


class Business(models.Model):
    business_name = models.CharField(max_length=50)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete = models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    email = models.EmailField(null=True) 
    description = models.TextField(null=True)   
    picture = CloudinaryField('image', default='')   

    @classmethod
    def display(cls):
        business= cls.objects.all()
        return business

    def __str__(self) :
        return f'{self.business_name}business'    

    def create_business(self):
        self.create_business()   

    def save_business(self):
        self.user
    def delete_business(self):
        self.delete()
    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(title__icontains=name).all() 


         
    
     


    
    
