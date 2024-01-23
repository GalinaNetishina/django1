from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['PATCH', 'DELETE'] and request.user.groups.filter(name='admins').exists():
            return True
        return request.user == obj.creator


class IsNotOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user != obj.creator
