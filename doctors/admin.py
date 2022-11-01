from django.contrib import admin
from .models import Doctor, Information
from accounts.models import User
# Register your models here.
# admin.site.register(Doctor)
admin.site.register(User)




class InformationInline(admin.StackedInline):
    model = Information
    fields =['address','image','shift','sec_images','about','active']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    inlines = [InformationInline]
    list_display = ['first_name','last_name','licenses','email']
    # actions = [make_deactive_product,make_active_product]
    list_filter = ('licenses',)
    search_fields = ('licenses','last_name')