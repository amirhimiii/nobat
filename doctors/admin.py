from django.contrib import admin
from .models import Doctor
from accounts.models import User
# Register your models here.
admin.site.register(Doctor)
admin.site.register(User)