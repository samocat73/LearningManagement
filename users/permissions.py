from rest_framework.permissions import BasePermission


class IsModer(BasePermission):
    """
    Проверяет, является ли пользователь модератором.
    """

    def has_permission(self, request, view):
        user = request.user
        return user.groups.filter(name="moderators").exists()


class IsOwner(BasePermission):
    """
    Проверяет, является ли пользователь владельцем.
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
