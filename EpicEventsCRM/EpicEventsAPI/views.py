from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Client, Contract, Event
from .serializers import ClientSerializer, ContractSerializer, EventSerializer
from . import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied


class ClientViewSet(viewsets.ModelViewSet):
    """Client ViewSet"""

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [
        IsAuthenticated,
        permissions.salesPermissions,
    ]
    lookup_field = "pk"
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    search_fields = [
        "email",
        "company_name",
    ]
    filterset_fields = [
        "email",
        "company_name",
    ]

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(sales_contact=author)


class ContractViewSet(viewsets.ModelViewSet):
    """Contract ViewSet"""

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [
        IsAuthenticated,
        permissions.salesPermissions,
    ]
    lookup_field = "pk"
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    search_fields = ["client__company_name", "client__email", "date_created", "amount"]
    filterset_fields = [
        "client__company_name",
        "client__email",
        "date_created",
        "amount",
    ]

    def perform_create(self, serializer):
        client = Client.objects.get(id=serializer.validated_data["client"].id)
        if client.sales_contact.id == self.request.user.id:
            contract = serializer.save(sales_contact=self.request.user)
        else:
            raise PermissionDenied(
                "You are not responsible of this client. As a result, you can't create a contract."
            )


class EventViewSet(viewsets.ModelViewSet):
    """Event ViewSet"""

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        IsAuthenticated,
        permissions.eventPermissions,
    ]
    lookup_field = "pk"
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    search_fields = ["client__email", "client__company_name", "event_date"]
    filterset_fields = ["client__email", "client__company_name", "event_date"]

    def perform_create(self, serializer):
        client = Client.objects.get(id=serializer.validated_data["client"].id)
        if client.sales_contact.id == self.request.user.id:
            contract = Contract.objects.get(
                sales_contact=self.request.user, client=client
            )
            if contract.status == True:
                event = serializer.save()
            else:
                raise PermissionDenied(
                    "No contract has been signed between you and the client. Impossible to create an event  for it."
                )
        else:
            raise PermissionDenied(
                "You are not responsible of this client. As a result, you can't create an event."
            )
