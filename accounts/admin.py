from django.contrib import admin
from authtools.admin import (
    UserAdmin, BASE_FIELDS, ADVANCED_PERMISSION_FIELDS, DATE_FIELDS,
)
from .models import EncampUser


class EncampUserAdmin(UserAdmin):
    ADDRESS_FIELDS = (
        'Address',
        {'fields': ('street_address', 'city', 'state', 'zip_code')}
    )
    fieldsets = (
        BASE_FIELDS,
        ADVANCED_PERMISSION_FIELDS,
        ADDRESS_FIELDS,
        DATE_FIELDS,
    )
    list_display = ('is_active', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff',)
    list_display_links = ('email', 'first_name', 'last_name',)
    search_fields = ('email', 'first_name', 'last_name',)


admin.site.register(EncampUser, EncampUserAdmin)
