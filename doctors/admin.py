from django.contrib import admin
from .models import Doctor, Information
from accounts.models import User
# Register your models here.
# admin.site.register(Doctor)
admin.site.register(User)
# admin.site.register(Information)





# @admin.register(Information)
class InformationInline(admin.StackedInline):
    model = Information
    fields =['user','doctor','address','image','shift','sec_images','about','active']
    list_display = ['user']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    inlines = [InformationInline]
    list_display = ['first_name','last_name','licenses','email']
    list_filter = ('licenses',)
    search_fields = ('licenses','last_name')
