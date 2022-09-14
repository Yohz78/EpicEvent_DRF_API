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
router.register(r"contracts", ContractViewSet)
router.register(r"events", EventViewSet)

urlpatterns = [
    path(r"", include(router.urls)),
]
