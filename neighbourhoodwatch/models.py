from django.db import models
from django.contrib.auth.models import User



    



class Profile(models.Model):
    name =models.CharField(max_length=50, blank=True)  
    id = models.CharField(max_length=50, blank=True, primary_key=True)
    # neighbourhood = models.ForeignKey(Neighbourhood, on_delete = models.CASCADE, primary_key=True)
    email = models.EmailField(null=True) 
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=300, default='') 

    def __str__(self):
        return f'{self.user.username} Profile'    

         
    
     


    
    
