from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

# Django Model Custom Fields
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    country = CountryField()

    address= models.TextField(blank=True)
    state= models.CharField(max_length=25,blank=True)
    city = models.CharField(max_length=25,blank=True)

    zip_code = models.CharField(
                _("zip code"), 
                max_length=5,
                null=True)
    
    phone_number = PhoneNumberField(
                    unique=True,
                    null=True)

    profile_image = models.ImageField(
                        default='/static/images/default_profile_image.jpg',
                        upload_to='profile_pic')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    