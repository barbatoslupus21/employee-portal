from django.contrib import admin
from .models import TicketCategory, TicketLevel, DeviceInformation, MISTickets


admin.site.register(TicketCategory)
admin.site.register(TicketLevel)
admin.site.register(DeviceInformation)
admin.site.register(MISTickets)
