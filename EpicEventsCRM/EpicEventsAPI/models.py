from django.db import models
from django.conf import settings


class Client(models.Model):
    """Client model"""

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=False, blank=True)
    sales_contact = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class Contract(models.Model):
    """Contract model"""

    sales_contact = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=False, blank=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField(max_length=11)
    payment_due = models.DateTimeField(auto_now_add=False)


class Event(models.Model):
    """Event model"""

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=False, blank=True)
    support_contact = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    # event_status = ??????
    attendees = models.IntegerField()
    event_date = models.DateTimeField(auto_now_add=False)
    notes = models.TextField(max_length=1000)
