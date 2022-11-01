from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import Information
from django.utils.translation import gettext_lazy as _





class CustomUserSerializer(serializers.ModelSerializer):
    province = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    licenses = serializers.CharField(read_only=True)
    sys_number = serializers.IntegerField(read_only=True)


    url = serializers.HyperlinkedIdentityField(
        read_only=True,        
        lookup_field='slug',
        view_name='doctor-detail'
    )
    class Meta:    
        model = get_user_model()
        fields = ['url','first_name','last_name','province','licenses','sys_number']



    def get_province(self):
        return self.province.value()





class CustomUserDetail(serializers.ModelSerializer):
    # user = CustomUserSerializer(required=False)
    # image = serializers.ImageField(allow_empty_file=True)
    class Meta:    
        model = Information
        fields = ['address','image','shift','sec_images','about']


    def update(self,instance ,validated_data):
            instance.address = validated_data.get('address',instance.address)
            instance.image = validated_data.get('image',instance.image)
            instance.shift = validated_data.get('shift',instance.shift)
            instance.sec_images = validated_data.get('sec_images',instance.sec_images)
            instance.about = validated_data.get('about',instance.about)
            instance.save()
            return instance   
        
        