from django.test import TestCase
from .models import Image
from users.models import User


class ImageTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.user1 = User(username="master")
        self.user1.save()
        self.image = Image(image='loisem',image_name='environment',image_caption='WOW!',profile=self.user1)

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,  Image))

    #Testing the save method
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    #Testing the delete method
    def test_delete_method(self):
        self.image2 = Image(image='loisem',image_name='Love',image_caption='Love is Blind',profile=self.user1)
        self.image2.save_image()
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertEqual(len(images),1)


