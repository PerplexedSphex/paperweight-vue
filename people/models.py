import uuid as uuid_lib
from django.db import models

from core.models import EncampBaseModel, AddressMixin


class Person(AddressMixin, EncampBaseModel):
    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'people'

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField('email address', max_length=255, null=True, blank=True)

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)
