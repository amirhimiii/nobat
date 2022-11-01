from django.db import models
from accounts.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _





# class Doctor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     licenses = models.CharField(choices= DOCTOR_LICENSES ,max_length=50) 

#     email = models.EmailField(_("email"),max_length=254,unique=True, blank=True , null=True )
#     province = OstanField(null=True, blank=True)

#     number = PhoneNumberField(verbose_name='phone number')
#     sys_number = models.IntegerField(_("Med-System number"),null=True, blank=True)
#     slug = models.SlugField()
    
    
    # def __str__(self):
    #     return self.user.username
    

