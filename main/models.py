from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Image(models.Model):
    '''
    This model will contain the columns to our image class
    '''
    image = models.ImageField(upload_to='main_photos/')
    image_name = models.CharField(max_length=30)
    image_caption=models.CharField(max_length=300,blank=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        '''
        Gets the absolute url for the Image created so as to enable redirect to image created route
        '''
        return reverse('image_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.image_name

    
    def save_image(self):
        '''
        Saves an Image in the db
        '''
        self.save()

    
    def delete_image(self):
        '''
        Deletes an image model from the db
        '''
        self.delete()

    
    def update_caption(self):
        '''
        Saves a caption from the db
        '''
        pass

    @classmethod
    def search_by_name(self,searched_image):
        '''
        Searches for images using names
        '''
        searched_images = self.objects.filter(image_name__icontains=searched_image)
        return searched_images

class Likes(models.Model):
    '''
    This model will contain the columns to our likes class
    '''
    image_like = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    
    def __int__(self):
        return self.like


class Comment(models.Model):
    '''
    This model will contain the columns for our comments class
    '''
    comment = models.CharField(max_length=255,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment





