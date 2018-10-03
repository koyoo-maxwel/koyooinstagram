from django.db import models

# Create your models here.







class Image(models.Model):
    name = models.CharField(max_length =60)
    caption = models.CharField(max_length =60)
    # profile = models.ForeignKey(Profile)
    likes = models.PositiveIntegerField()
    image = models.ImageField(upload_to = 'images/', blank=True, null=True)


    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

