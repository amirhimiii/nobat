from django.shortcuts import render
from .models import Doctor , Information
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model

#allauth
from .forms import DoctorSignupForm
from allauth.account.views import SignupView

#rest
from .models import Information
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import CustomUserSerializer,DoctorDetailSerializer,CreateInformationSerializer
from .permissions import UserPermissions, UserUpdatePermissions
from rest_framework.fields import CurrentUserDefault
from django.db.models import Q
from itertools import chain




class DoctorView(SignupView):
    """
    allauth signup form for doctors
    """

    template_name = 'account/signup.html'
    form_class = DoctorSignupForm
    view_name = 'doctor_signup'
    success_url = reverse_lazy('information-create')



doctor_signup = DoctorView.as_view()





# Doctors Section

class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [UserPermissions]
    
doctor_list = DoctorListView.as_view()



class DoctorCreateViews(generics.CreateAPIView):
    serializer_class = CreateInformationSerializer 
    permission_classes = [UserUpdatePermissions]

    def get_queryset(self):
        # user2 = self.request.user
        slug = self.kwargs.get('slug')        
        # queryset =Information.objects.create(user=get_user_model(),user__slug=slug)
        # queryset =Information.objects.add(doctor__user=user2,user=get_user_model())
        queryset =Information.objects.add(doctor__user=user2,user=get_user_model())

        return queryset

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            user = serializer.save(doctor=self.request.user.doctor)
        else:
            user = serializer.save()    

doctor_create = DoctorCreateViews.as_view()




class RetriveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorDetailSerializer
    permission_classes = [UserUpdatePermissions]
    lookup_field = 'slug`'

    def get_object(self):
        slug = self.kwargs['slug']
        get_user = self.request.POST.get('doctor')
        info = Information.objects.select_related('doctor').get(doctor__slug=slug)
        return info



detail_update_delete = RetriveUpdateDelete.as_view()


#tamiz kardan code
#yeki kardan user o doctor dakhel model / chon tonestam ba code usero begirm dg niazi be field user nist
#