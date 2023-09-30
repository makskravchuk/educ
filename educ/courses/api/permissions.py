from rest_framework import permissions


class IsEnrolled(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.students.filter(id=request.user.id).exists()