from django.shortcuts import render
from .forms import DoctorSignupForm
from allauth.account.views import SignupView





class DoctorView(SignupView):
    template_name = 'account/signup.html'
    form_class = DoctorSignupForm
    view_name = 'doctor_signup'
    


doctor_signup = DoctorView.as_view()