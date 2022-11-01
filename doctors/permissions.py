from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS



class UserPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or 
            request.user.is_authenticated  
        )




class UserUpdatePermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            request.user== obj.user or request.user.is_staff
            )
        