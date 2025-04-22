from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    firstname = models.CharField(max_length = 50 , blank  = True, null = True)
    lastname = models.CharField(max_length = 50 , blank  = True, null = True)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='profile_photos' ,blank=True, null=True)
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        # else:
        return " "
    
    # userphoto=models.ImageField(upload_to='user_images', blank=True,null=True)

    # def __str__(self):
    #     return self.user.firstname
class Temple(models.Model):
    name = models.CharField(max_length = 100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    image = models.ImageField(upload_to='temple_images')
    short_description = models.CharField(max_length = 100 , null=True, default ="ॐ नमः शिवाय")
    description =models.TextField()
    # DeitiesWorship
    history =models.TextField(null=True, blank=True)
    significance =models.TextField(null=True, blank=True)
    architecture =models.TextField(null=True, blank=True)
    opening_closing_time = models.CharField(max_length=500, null=True, blank=True)
    howtoreach=models.TextField(null=True,blank=True)
    address = models.CharField(max_length=300,null=True)
    latitude = models.FloatField(null=True ,blank=True)
    longitude = models.FloatField(null=True,blank = True)

    def __str__(self):
        return self.name
        
class Feedback(models.Model):
    content=models.TextField()
    # submitted_by_user=models.BooleanField(default=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE, related_name="user_feedbacks",null=True)
    content_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"feedback #{self.pk}"

    
