from rest_framework.permissions import BasePermission

class IsDirigeant(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Dirigeant').exists()
