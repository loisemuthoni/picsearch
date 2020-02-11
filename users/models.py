from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    '''
    Creates fields that will be needed for the user profile
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio  = models.CharField(max_length=200,blank=True) 

    def __str__(self):
        return f'{self.user.username} Profile'