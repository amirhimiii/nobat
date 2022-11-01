from django.shortcuts import render
from .models import Doctor , Information

#allauth
from .forms import DoctorSignupForm
from allauth.account.views import SignupView

#rest
from .models import Information
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import CustomUserSerializer,CustomUserDetail
from .permissions import UserPermissions, UserUpdatePermissions





class DoctorView(SignupView):
    """
    allauth signup form for doctors
    """

    template_name = 'account/signup.html'
    form_class = DoctorSignupForm
    view_name = 'doctor_signup'
    

doctor_signup = DoctorView.as_view()


# tarif view hay rest (retrieve , update, list, destroy)



class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [UserPermissions]
    
doctor_list = DoctorListView.as_view()



class DoctorRetriveUpdateViews(generics.RetrieveUpdateAPIView):
    serializer_class = CustomUserDetail 
    permission_classes = [UserUpdatePermissions]

    def get_object(self):
        user = self.request.user
        slug = self.kwargs.get('slug')
        queryset = Information.objects.select_related('user').get(user__slug=slug)
        return queryset



doctor_view = DoctorRetriveUpdateViews.as_view()