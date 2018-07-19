import uuid as uuid_lib
from django.db import models
from authtools.models import AbstractEmailUser

from core.models import AddressMixin


class User(AddressMixin, AbstractEmailUser):
    """Creating this now so it's easier to customize later without borking the db"""
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, unique=True, editable=False)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    account_holder = models.ForeignKey(
        'accounts.AccountHolder',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        editable=False,
        help_text='Entity that has an account with Encamp with which this user is associated.'
    )

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return '{name} <{email}>'.format(
            name=self.name,
            email=self.email,
        )

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name


class AccountHolder(models.Model):
    """Basic tenant entity for multitenanting.
    All records except for users should have a foreign key to this model."""
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, unique=True, editable=False)

    name = models.CharField(max_length=255)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
