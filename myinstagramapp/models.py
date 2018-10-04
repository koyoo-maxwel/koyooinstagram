from django.contrib.auth.models import User
from django.db import models
import datetime as dt


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=200)
    profile_pic = models.ImageField(
        upload_to='profile/')
    time_stamp = models.DateTimeField(auto_now_add=True, null=True)
   


   
    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def search_profile(cls, query):
        profile = cls.objects.filter(user__username__icontains=query)
        return profile

        

    # my images registerd here
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.TextField(blank=True)
    likes = models.PositiveIntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
 
    class Meta:
        ordering = ['-time']
   

    def save_images(self):
        self.save()

    def total_likes(self):
        return self.likes.count()

    def save_comment(self):
            self.save()

