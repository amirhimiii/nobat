from allauth.account.forms import SignupForm
from phonenumber_field.formfields import PhoneNumberField

from .models import Customer
from django import forms




class UserSignupForm(SignupForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()
    number = PhoneNumberField(region="IR")

    def save(self, request):
        user = super(UserSignupForm, self).save(request)
        customer = Customer(
            user=user,
            age=self.cleaned_data.get('age'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            number=self.cleaned_data.get('number'),
        )
        customer.save()

        return customer.user