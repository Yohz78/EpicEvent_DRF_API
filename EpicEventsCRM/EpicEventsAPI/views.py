from rest_framework import viewsets

from .models import Client, Contract, Event
from .serializers import ClientSerializer, ContractSerializer, EventSerializer
from . import permissions
from rest_framework.permissions import IsAuthenticated


class ClientViewSet(viewsets.ModelViewSet):
    """Client ViewSet"""

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [
        IsAuthenticated,
        permissions.clientPermissions,
    ]
    lookup_field = "pk"

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(sales_contact=self.request.user)
        return query_set


class ContractViewSet(viewsets.ModelViewSet):
    """Contract ViewSet"""

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [
        IsAuthenticated,
        permissions.contractPermissions,
    ]
    lookup_field = "pk"


class EventViewSet(viewsets.ModelViewSet):
    """Event ViewSet"""

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        IsAuthenticated,
        permissions.eventPermissions,
    ]
    lookup_field = "pk"
