from rest_framework.permissions import BasePermission


class IsActiveUser(BasePermission):
    """
    Проверка на флаг is_active у пользователя
    """

    def has_permission(self, request, view):
        return request.user.is_active
