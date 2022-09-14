from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

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
        permissions.salesPermissions,
    ]
    lookup_field = "pk"
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(sales_contact=self.request.user)
        return query_set

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

    def perform_create(self, serializer):
        author = self.request.user
        client = Client.objects.get(pk=self.kwargs["client__pk"])
        serializer.save(sales_contact=author, client=client)


class EventViewSet(viewsets.ModelViewSet):
    """Event ViewSet"""

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        IsAuthenticated,
        permissions.eventPermissions,
    ]
    lookup_field = "pk"

    def perform_create(self, serializer):
        client = Client.objects.get(pk=self.kwargs["client__pk"])
        serializer.save(client=client)
