from rest_framework import permissions
from account.models import MyUser


class CustomPermissions(permissions.BasePermission):
    edit_methods = ("POST", "PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == MyUser.EMPLOYEE:
            try:
                if request.method == 'DELETE':
                    return False
            except:
                pass
            return True
        if request.user.is_authenticated and request.user.role == MyUser.MANAGER:
            return True
        if request.user.is_authenticated and request.user.role == MyUser.USER:
            try:
                if view.action == 'create':
                    return False
            except:
                pass
            try:
                if request.method == 'POST' or request.method == 'DELETE':
                    return False
            except:
                pass

            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.role == MyUser.MANAGER or request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role == MyUser.EMPLOYEE and request.method in self.edit_methods:
            return True

        return False
