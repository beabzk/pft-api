from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Allow access only if the requesting user owns the object.
    Applies to both read and write operations on object-level routes.
    """
    def has_object_permission(self, request, view, obj):
        # For both SAFE_METHODS and writes, require ownership.
        return getattr(obj, 'user', None) == getattr(request, 'user', None)
