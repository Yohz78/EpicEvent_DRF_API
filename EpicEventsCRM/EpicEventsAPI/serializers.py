from rest_framework import serializers
from .models import Client, Contract, Event


class ClientSerializer(serializers.ModelSerializer):
    """Client model Serializer"""

    class Meta:
        model = Client
        fields = [
            "pk",
            "first_name",
            "last_name",
            "email",
            "phone",
            "mobile",
            "company_name",
            "date_created",
            "date_updated",
            "sales_contact",
        ]


class ContractSerializer(serializers.ModelSerializer):
    """Contract model Serializer"""

    class Meta:
        model = Contract
        fields = [
            "pk",
            "sales_contact",
            "client",
            "date_created",
            "date_updated",
            "status",
            "amount",
            "payment_due",
        ]


class EventSerializer(serializers.ModelSerializer):
    """Event model Serializer"""

    class Meta:
        model = Event
        fields = [
            "pk",
            "client",
            "created_time",
            "date_created",
            "date_updated",
            "support_contact",
            "attendees",
            "event_date",
            "status",
            "notes",
        ]
