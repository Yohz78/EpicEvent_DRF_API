from rest_framework import viewsets

from .models import Client, Contract, Event
from .serializers import ClientSerializer, ContractSerializer, EventSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """Client ViewSet"""

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = "pk"


class ContractViewSet(viewsets.ModelViewSet):
    """Contract ViewSet"""

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    lookup_field = "pk"


class EventViewSet(viewsets.ModelViewSet):
    """Event ViewSet"""

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = "pk"
