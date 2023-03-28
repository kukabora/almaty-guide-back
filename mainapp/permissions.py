from rest_framework import permissions


class CustomModelPermission(permissions.BasePermission):
    """
    Custom permission to only allow admin users to perform CREATE, UPDATE, and DELETE operations.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='Admin').exists()
