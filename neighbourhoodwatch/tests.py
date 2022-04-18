
from django.test import TestCase
from requests import post
from .models import Business, Neighbourhood, Profile, Post

# Set up method 
# Set up method 
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile=Profile(name='juliet')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

#Testing Save Method

    

    

# Set up method        


class PostTestClass(TestCase):
    def setUp(self):
        self.post=Post(post='hey')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post)) 


    def test_save_post(self):
        
        self.post.save()
        self.assertEqual(len(post.save),1)       



#  Set up method   

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.neighbourhood=Neighbourhood(name='juliet')

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))  

class BusinessTestClass(TestCase):
    def setUp(self):
        self.business=Business(picture='image')

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))           





        





        



