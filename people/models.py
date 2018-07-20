from django.db import models

from core.models import EncampBaseModel, AddressMixin


class UserPersonMixin(AddressMixin):
    """A mixin to hold fields common to User and Person models

    When updating this model, remember to update the docstring of the
    User model so it remains accurate.

    The purpose of this is to ensure consistency between these info fields
    so that 'linking' Users and People together can save on double-entering
    data. Information can automatically flow when Users make changes
    to all 'linked' Person records.
    Email address will have to be handled as a special case since it is
    the 'username' field of the User model.
    UUIDs and record_owners obviously will not flow.
    """
    class Meta:
        abstract = True
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Person(UserPersonMixin, EncampBaseModel):
    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'people'

    email = models.EmailField('email address', max_length=255, null=True, blank=True)
