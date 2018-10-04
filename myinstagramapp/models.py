from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=True)

    class Meta:
        ordering = ['-name']

    def save_tag(self):
        self.save()



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile-pictures/')
    



    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def search_profiles(cls, name):
        profile = cls.objects.filter(user__username__icontains=name)
        return profile





class Comment(models.Model):
    text = models.CharField(max_length=250, blank=True)
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    # post = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    time_posted = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-time_posted']
    def save_comment(self):
        self.save()

    def __str__(self):
        return self.text




class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.TextField(blank=True)
    likes = models.PositiveIntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
   

    class Meta:
        ordering = ['-time']

    def save_images(self):
        self.save()

    def total_likes(self):
        return self.likes.count()

