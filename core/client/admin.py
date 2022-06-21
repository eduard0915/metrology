from django.contrib import admin

from core.client.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'nit_client', 'address_client', 'phone_client', 'mail_client', 'contact_client', 'active_client'
    )


# Register your models here.
admin.site.register(Client, ClientAdmin)
