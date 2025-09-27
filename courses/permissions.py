from rest_framework.permissions import BasePermission
#кастомное пермишин 
class IsTeacher(BasePermission):#разрешено доступ только учителям
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role =='teacher'