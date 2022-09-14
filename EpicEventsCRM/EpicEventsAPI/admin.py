from django.contrib import admin

from django.contrib import admin
from .models import Event, Contract, Client

admin.site.register(Event)
admin.site.register(Contract)
admin.site.register(Client)
