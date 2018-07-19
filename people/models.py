from django.db import models

from core.models import TenantMixin, AddressMixin


class Person(TenantMixin, AddressMixin, models.Model):
    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'people'

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField('email address', max_length=255, null=True, blank=True)

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)
