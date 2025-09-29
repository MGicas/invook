from rest_framework.permissions import BasePermission

class OnlyAdminAccess(BasePermission):
    message = "Solo los usuarios con rol ADMIN pueden acceder a este recurso."

    def has_permission(self, request, view):
        u = request.user
        return bool(u and u.is_authenticated and getattr(u, "role", "UNKNOWN") == "ADMIN")
    

class OnlyAdminDeleteHardware(BasePermission):
    message = "Solo los usuarios con rol ADMIN pueden eliminar hardware."

    def has_permission(self, request, view):
        if request.method == "DELETE":
            u = request.user
            return bool(u and u.is_authenticated and getattr(u, "role", "UNKNOWN") == "ADMIN")
        return True
    
class OnlyAdminDeleteSupply(BasePermission):
    message = "Solo los usuarios con rol ADMIN pueden eliminar supply."

    def has_permission(self, request, view):
        if request.method == "DELETE":
            u = request.user
            return bool(u and u.is_authenticated and getattr(u, "role", "UNKNOWN") == "ADMIN")
        return True
