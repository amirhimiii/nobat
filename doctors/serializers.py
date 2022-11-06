from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import Information , Doctor
from django.utils.translation import gettext_lazy as _
from rest_framework.fields import CurrentUserDefault





class CustomUserSerializer(serializers.ModelSerializer):
    province = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    licenses = serializers.CharField(read_only=True)
    sys_number = serializers.IntegerField(read_only=True)


    url = serializers.HyperlinkedIdentityField(
        read_only=True,        
        lookup_field='slug',
        view_name ='detail-update-delete'
    )
    class Meta:    
        model = get_user_model()
        fields = ['url','first_name','last_name','province','licenses','sys_number']


    def get_province(self):
        return self.province.value()





SHIFT_CHOICES = [
        ('online','online'),
        ('phone','phone'),
        ('phone & online','phone & online'),
    ]

class CreateInformationSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # doctor = serializers.HiddenField(default=serializers.CurrentUserDefault())
    address = serializers.CharField()
    image = serializers.ImageField()
    shift =  serializers.ChoiceField(choices=SHIFT_CHOICES)
    sec_images = serializers.FileField(allow_empty_file =True)
    about = serializers.CharField()
    active = serializers.BooleanField()
    datetime_created = serializers.DateTimeField()

    def create(self, validated_data):
        return Information.objects.create(**validated_data)




class DoctornSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'



class DoctorDetailSerializer(serializers.ModelSerializer):
    doctor = DoctornSerializer(required=False)
    # image = serializers.ImageField(allow_empty_file=True)
    class Meta:    
        model = Information
        fields ='__all__'
        # fields = ['information']
        # read_only_fields = ('user',)










    # def update(self,instance ,validated_data):
    #         instance.user = validated_data.get('user',instance.user)
    #         instance.address = validated_data.get('address',instance.address)

    #         instance.image = validated_data.get('image',instance.image)
            
    #         instance.shift = validated_data.get('shift',instance.shift)
    #         instance.sec_images = validated_data.get('sec_images',instance.sec_images)
    #         instance.about = validated_data.get('about',instance.about)
    #         # if instance.is_valid(raise_exception=True):

    #         instance.save()
    #         return instance   
        
        