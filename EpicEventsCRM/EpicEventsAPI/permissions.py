from rest_framework import permissions
from . import models


class clientPermissions(permissions.BasePermission):
    """
    Define client model permissions.
    """

    def has_permission(self, request, view):
        if request.user.role == "staff" and request.method in permissions.SAFE_METHODS:
            return True

        if request.user.role == "sales":
            return True

    def has_object_permission(self, request, view, obj):
        if request.user == obj.sales_contact:
            return True

        if request.user.role == "sales" and request.method in permissions.SAFE_METHODS:
            return True

        if request.user.role == "staff" and request.method in permissions.SAFE_METHODS:
            return True

        if request.user.role == "support":
            event = models.Event.objects.filter(
                support_contact=request.user, client=obj.id
            )
            if event and request.method in permissions.SAFE_METHODS:
                return True


class contractPermissions(permissions.BasePermission):
    """
    Define contract model permissions.
    """

    def has_permission(self, request, view):
        client = models.Client.objects.get(pk=view.kwargs["client__pk"])
        if request.user == client.sales_contact:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user == obj.sales_contact:
            return True


class eventPermissions(permissions.BasePermission):
    """
    Define event model permissions.
    """

    def has_permission(self, request, view):
        contract = models.Contract.objects.get(pk=view.kwargs["contract__pk"])
        if request.user == contract.sales_contact:
            return True

    def has_object_permission(self, request, view, obj):
        if (
            request.user == obj.client.sales_contact
            or request.user == obj.support_contact
        ):
            return True
