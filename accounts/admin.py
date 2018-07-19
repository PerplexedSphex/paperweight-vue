import copy
from django.contrib import admin
from authtools.admin import (
    UserAdmin, BASE_FIELDS, ADVANCED_PERMISSION_FIELDS, DATE_FIELDS,
)
from .models import User, AccountHolder
from core.models import AddressMixin


class EncampUserAdmin(UserAdmin):
    PERMISSION_FIELDS = copy.deepcopy(ADVANCED_PERMISSION_FIELDS)
    PERMISSION_FIELDS[1]['fields'] = ('account_holder',) + PERMISSION_FIELDS[1]['fields']
    fieldsets = (
        BASE_FIELDS,
        PERMISSION_FIELDS,
        AddressMixin.ADMIN_FIELDSET,
        DATE_FIELDS,
    )
    list_display = ('is_active', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff',)
    list_display_links = ('email', 'first_name', 'last_name',)
    search_fields = ('email', 'first_name', 'last_name',)


admin.site.register(User, EncampUserAdmin)
admin.site.register(AccountHolder)
