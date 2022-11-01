from allauth.account.forms import SignupForm
from iranian_cities.fields import OstanField
from phonenumber_field.formfields import PhoneNumberField

from .models import DOCTOR_LICENSES
from .models import Doctor
from django import forms


class DoctorSignupForm(SignupForm):
    """
    override allauth signupform
    """
    
    email = forms.EmailField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    number = PhoneNumberField(region="IR")
    licenses = forms.ChoiceField(choices=DOCTOR_LICENSES)
    sys_number = forms.IntegerField()



    def save(self, request):
        user = super(DoctorSignupForm, self).save(request)
        doctor = Doctor(
            user=user,
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            number=self.cleaned_data.get('number'),
            licenses=self.cleaned_data.get('licenses'),
            sys_number=self.cleaned_data.get('sys_number'),
            email=self.cleaned_data.get('email'),

        )
        doctor.save()
        return doctor.user