from django.shortcuts import render
from allauth.account.views import SignupView
from .forms import UserSignupForm



class Customer(SignupView):
    template_name = 'account/signup.html'
    form_class = UserSignupForm
    view_name = 'customer_signup'

customer_signup = Customer.as_view()



