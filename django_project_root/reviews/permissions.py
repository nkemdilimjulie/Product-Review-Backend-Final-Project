from rest_framework import permissions
from django.core.exceptions import PermissionDenied


# only authenticated users can acces list API view, detail API view    
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Authenticated users can access list view
        if request.user.is_authenticated:
            return True
        return False

    # permission for detail API view: 
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:            
            # Write permissions are only allowed to the author of review
            return obj.author == request.user
