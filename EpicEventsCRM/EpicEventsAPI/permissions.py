from operator import truediv
from rest_framework import permissions
import logging

logger = logging.getLogger(__name__)


class salesPermissions(permissions.BasePermission):
    """
    Define contracts and clients permissions.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.role == "sales" and request.method != "DELETE":
            return True

        if request.user.role == "staff" and request.method != "POST":
            return True

    def has_object_permission(self, request, view, obj):
        try:
            if request.method in permissions.SAFE_METHODS:
                return True

            if request.user == obj.sales_contact:
                return True

            if (
                request.user.role == "sales"
                and request.method in permissions.SAFE_METHODS
            ):
                return True

            if request.user.role == "staff" and request.method != "DELETE":
                return True
        except:
            logger.warning("User tried a forbbiden method.")
            return False


class eventPermissions(permissions.BasePermission):
    """
    Define event model permissions.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role == "sales" and request.method != "DELETE":
            return True
        if request.user.role in ["support", "staff"] and request.method != "POST":
            return True

    def has_object_permission(self, request, view, obj):
        try:
            if request.method in permissions.SAFE_METHODS:
                return True
            if (
                request.user == obj.client.sales_contact
                or request.user == obj.support_contact
                and request.method != "DELETE"
            ):
                return True
        except:
            logger.warning("User tried a forbbiden method.")
            return False
