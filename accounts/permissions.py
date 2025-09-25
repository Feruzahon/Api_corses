from  rest_framework import permissions

class IsAuthenticateUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    

class IsNotAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user  or not request.user.is_authenticated