from django.db import models
from accounts.models import User
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from iranian_cities.fields import OstanField



DOCTOR_LICENSES = {
        ('dr','Doctor'),
        ('au','Authority')
    }

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    licenses = models.CharField(choices= DOCTOR_LICENSES ,max_length=50) 

    email = models.EmailField(_("email"),max_length=254,unique=True, blank=True , null=True )
    province = OstanField(null=True, blank=True)

    number = PhoneNumberField(verbose_name='phone number')
    sys_number = models.IntegerField(_("Med-System number"),null=True, blank=True)
    slug = models.SlugField()
    
    
    # def __str__(self):
    #     return self.user.username
    

class Information(models.Model):
    SHIFT_CHOICES = [
        ('online','online'),
        ('phone','phone'),
        ('phone & online','phone & online'),
    ]
    
    user = models.OneToOneField(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE,blank=True ,null=True,related_name='users')
    address = models.TextField(_("address"),null=True,blank=True)
    image = models.ImageField(_("profile photo"), upload_to='image/personal_image/',null=True,blank=True)
    shift = models.CharField(_("taking turns online/phone"),choices =SHIFT_CHOICES ,max_length=20,null=True,blank=True)
    sec_images = models.FileField(_("additional files"),null=True,blank=True ,upload_to='image/file/',max_length=100)   
    about = models.TextField(_("about me"),null=True,blank=True)
    active =models.BooleanField(_("active user?"), default=True)
    datetime_created = models.DateTimeField(_("date created"), auto_now=True)


    class Meta:
        verbose_name = _("informations")
        verbose_name_plural = _("informations")