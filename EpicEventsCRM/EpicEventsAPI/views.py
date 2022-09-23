from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from EpicEventsUsers.models import CustomUser
from .models import Client, Contract, Event
from .serializers import ClientSerializer, ContractSerializer, EventSerializer
from . import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
import logging

logger = logging.getLogger(__name__)


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
            logger.warning(
                "User tried to create a contract while not being responsible of the client"
            )
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
                support_contact = CustomUser.objects.get(
                    id=serializer.validated_data["support_contact"].id
                )
                if support_contact.role == "support":
                    event = serializer.save()
                else:
                    logger.warning("This user is not a support team member.")
                    raise PermissionDenied(
                        "You have to select an User who is a member of the support team in order to create an event."
                    )
            else:
                logger.warning(
                    "User trying to create an event while no contract has been signed."
                )
                raise PermissionDenied(
                    "No contract has been signed between you and the client. Impossible to create an event  for it."
                )
        else:
            logger.warning(
                "User tryied to created an event while not being responsible of the client"
            )
            raise PermissionDenied(
                "You are not responsible of this client. As a result, you can't create an event."
            )

    def perform_update(self, serializer):
        support_contact = CustomUser.objects.get(
            id=serializer.validated_data["support_contact"].id
        )
        if support_contact.role == "support":
            event = serializer.save()
        else:
            logger.warning("This user is not a support team member.")
            raise PermissionDenied(
                "You have to select an User who is a member of the support team in order to create an event."
            )
