from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow creator of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        
        return obj.creator == request.user or str(request.user) == str(obj.receiver)
    
    def has_view_permission(self, request, view, obj):

        return obj.creator == request.user #or str(request.user) == str(obj.receiver)


class UserView(permissions.BasePermission):
    def has_view_permission(self, request, view, obj):
        self.check_object_permissions(self.request, obj)
        return False #obj.creator == request.user

    def has_add_permission(self, request, view, obj):
        self.check_object_permissions(self.request, obj)
        return False #obj.creator == request.user

    def has_delete_permission(self, request, view, obj):
        self.check_object_permissions(self.request, obj)
        return False #obj.creator == request.user
