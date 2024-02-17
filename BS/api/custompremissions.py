from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'Admin':
            return request.method in ['GET', 'POST', 'PUT', 'DELETE']
        return False

class IsManager(BasePermission):
    def has_permission(self, request, view):

        if request.user.role == 'Manager':
            return request.method in ['GET', 'POST']
        return False

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'Employee':
            return request.method == 'GET'
        return False  