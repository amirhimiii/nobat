from django.db import models
from accounts.models import User
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from iranian_cities.fields import OstanField
from django.utils.text import slugify
from django.urls import reverse_lazy, reverse

import random



rand_int = random.randint(100, 500_000)

DOCTOR_LICENSES = {
        ('dr','Doctor'),
        ('au','Authority')
    }




class Doctor(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    licenses = models.CharField(choices= DOCTOR_LICENSES ,max_length=50) 

    email = models.EmailField(_("email"),max_length=254,unique=True, blank=True , null=True )
    province = OstanField(null=True, blank=True)

    number = PhoneNumberField(verbose_name='phone number')
    sys_number = models.IntegerField(_("Med-System number"),null=True, blank=True)
    slug = models.SlugField()
    #acitve
    
    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.first_name}-{self.last_name}-{rand_int}')
        super().save(*args, **kwargs)




SHIFT_CHOICES = [
        ('online','online'),
        ('phone','phone'),
        ('phone & online','phone & online'),
    ]

class Information(models.Model):

    
    user = models.OneToOneField(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE,related_name='users')
    doctor = models.OneToOneField(Doctor, blank=True,null=True, on_delete=models.CASCADE,related_name='doctors',default=None)
    address = models.TextField(_("address"))
    image = models.ImageField(_("profile photo"),blank=False, null=True ,upload_to='image/personal_image/')
    shift = models.CharField(_("taking turns online/phone"),choices =SHIFT_CHOICES ,max_length=20)
    sec_images = models.FileField(_("additional files"),null=True,blank=True ,upload_to='image/file/',max_length=100)   
    about = models.TextField(_("about me"))
    active =models.BooleanField(_("active user?"), default=True)
    datetime_created = models.DateTimeField(_("date created"), auto_now=True)
    # slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    def get_absolute_url(self):
        return reverse('doctor-list')


    class Meta:
        verbose_name = _("informations")
        verbose_name_plural = _("informations")