from django.contrib import admin

from .models import Person
from core.models import AddressMixin


class PersonAdmin(admin.ModelAdmin):
    BASE_FIELDS = (None, {'fields': ('first_name', 'last_name', 'email')})
    fieldsets = (
        BASE_FIELDS,
        AddressMixin.ADMIN_FIELDSET,
    )


admin.site.register(Person, PersonAdmin)
