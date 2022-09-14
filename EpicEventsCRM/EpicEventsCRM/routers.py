from rest_framework import routers
from rest_framework_nested import routers
from django.urls import path, include
from EpicEventsAPI.views import (
    ClientViewSet,
    ContractViewSet,
    EventViewSet,
)


router = routers.DefaultRouter()
router.register(r"clients", ClientViewSet)

clients_router = routers.NestedSimpleRouter(router, r"clients", lookup="client")
clients_router.register(r"issues", ContractViewSet, basename="contract")
clients_router.register(r"users", EventViewSet, basename="event")

contract_router = routers.NestedSimpleRouter(
    clients_router, r"clients", lookup="client"
)
contract_router.register(r"events", EventViewSet, basename="event")

urlpatterns = [
    path(r"", include(router.urls)),
    path(r"", include(clients_router.urls)),
    path(r"", include(contract_router.urls)),
]
