from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Позволяет владельцу изменять объект, а остальным пользователям предоставляет только доступ для чтения.
    """

    def has_object_permission(self, request, view, obj) -> bool:
        """Проверяет, является ли текущий пользователь владельцем объекта."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
