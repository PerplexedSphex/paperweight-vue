from django.db import models
from authtools.models import AbstractNamedUser


class EncampUser(AbstractNamedUser):
    """Creating this now so it's easier to customize later without borking the db"""

    def __str__(self):
        return self.name


class AccountHolder(models.Model):
    """Basic tenant entity for multitenanting.
    All records except for users should have a foreign key to this model."""
    name = models.CharField(max_length=255)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
