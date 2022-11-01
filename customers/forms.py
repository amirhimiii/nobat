from allauth.account.forms import SignupForm
from .models import Customer
from django import forms




class UserSignupForm(SignupForm):

    age = forms.IntegerField()
first_name
last_name
age
number

    def save(self, request):
        user = super(UserSignupForm, self).save(request)
        customer = Customer(
            user=user,
            age=self.cleaned_data.get('age')
        )
        customer.save()

        return customer.user