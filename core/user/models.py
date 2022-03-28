from django.contrib.auth.models import AbstractUser
from django.db import models

from bpmprometro.settings import MEDIA_URL, STATIC_URL


# Usuarios
class User(AbstractUser):
    cedula = models.CharField(max_length=15, null=True, blank=True, unique=False, verbose_name='Cédula')
    cargo = models.CharField(max_length=50, null=True, blank=True, verbose_name='Cargo')
    email_person = models.EmailField(null=True, blank=True, verbose_name='Email Personal')
    cellphone = models.CharField(max_length=10, null=True, blank=True, verbose_name='N° Celular')
    address_user = models.CharField(max_length=50, null=True, blank=True, verbose_name='Dirección')
    date_birth = models.DateField(null=True, blank=True, verbose_name='Fecha de Nacimiento')
    photo = models.ImageField(upload_to='user/%Y%m%d', null=True, blank=True, verbose_name='Foto')

    def __str__(self):
        return f'{self.get_full_name()}, {self.cargo}'

    def get_image(self):
        if self.photo:
            return '{}{}'.format(MEDIA_URL, self.photo)
        return '{}{}'.format(STATIC_URL, 'img/default-avatar.jpg')
