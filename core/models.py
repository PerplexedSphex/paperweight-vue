from django.db import models

from .constants import State
from .managers import EncampBaseModelManager


class TenantMixin(models.Model):
    class Meta:
        abstract = True

    record_owner = models.ForeignKey(
        'accounts.AccountHolder',
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_owned_set",
        editable=False
    )
    objects = EncampBaseModelManager()


class AddressMixin(models.Model):
    class Meta:
        abstract = True

    full_address_raw = models.CharField(max_length=511, null=True, blank=True, editable=False)
    street_address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=127, null=True, blank=True)
    state = models.CharField(max_length=2, choices=State.MODEL_FIELD_CHOICES, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        address_array = []
        if self.street_address:
            address_array.append(self.street_address)
        if self.city:
            address_array.append(self.city)
        if self.state:
            address_array.append(self.state)
        if self.zip_code:
            address_array.append(str(self.zip_code))
        if address_array:
            self.full_address_raw = " ".join(address_array)
        super().save(*args, **kwargs)

    ADMIN_FIELDSET = (
        'Address',
        {'fields': ('street_address', 'city', 'state', 'zip_code')}
    )


class LatLonMixin(models.Model):
    """Not tested"""

    class Meta:
        abstract = True

    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
