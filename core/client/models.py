from crum import get_current_user
from django.db import models

from core.models import BaseModel


class Client(BaseModel):
    client = models.CharField(max_length=150, verbose_name='Cliente')
    nit_client = models.CharField(max_length=20, verbose_name='NIT', unique=True)
    address_client = models.CharField(max_length=300, verbose_name='Dirección')
    phone_client = models.CharField(max_length=50, verbose_name='Telefónos')
    mail_client = models.EmailField(verbose_name='E-mail')
    contact_client = models.CharField(max_length=300, verbose_name='Contacto')
    active_client = models.BooleanField(default=True, verbose_name='Activo', null=True, blank=True)

    def __str__(self):
        return self.client

    class Meta:
        db_table = 'Client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, *args, **kwargs):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        self.client = self.client.capitalize()
        self.contact_client = self.contact_client.capitalize()
        return super(Client, self).save(*args, **kwargs)
