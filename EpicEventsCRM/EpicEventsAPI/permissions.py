from rest_framework import permissions


class salesPermissions(permissions.BasePermission):
    """
    Define contracts and clients permissions.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.role == "sales":
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user == obj.sales_contact:
            return True

        if request.user.role == "sales" and request.method in permissions.SAFE_METHODS:
            return True

        if request.user.role == "staff" and request.method in permissions.SAFE_METHODS:
            return True


class eventPermissions(permissions.BasePermission):
    """
    Define event model permissions.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role == "sales":
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if (
            request.user == obj.client.sales_contact
            or request.user == obj.support_contact
        ):
            return True
