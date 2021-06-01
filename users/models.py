from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    country = CountryField()
    city = models.CharField(max_length=25)
    
    profile_image = models.ImageField(default='/staticfiles/images/default_profile_image.jpg', upload_to='profile_pic')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    