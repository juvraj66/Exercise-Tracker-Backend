from rest_framework import permissions


class IsAdminReadWrite(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS and request.user.is_staff:
            return True
        # Write permissions are only allowed to the creator of a exercise
        return obj.creator == request.user


class IsAdminWriteUserRead(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_superuser


class IsCreatorOrReadOnly1(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the creator of a exercise
        return obj.user == request.user
