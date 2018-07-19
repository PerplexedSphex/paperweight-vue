from django.contrib import admin
from authtools.admin import (
    UserAdmin, BASE_FIELDS, ADVANCED_PERMISSION_FIELDS, DATE_FIELDS,
)
from .models import User
from core.models import AddressMixin


class EncampUserAdmin(UserAdmin):
    fieldsets = (
        BASE_FIELDS,
        ADVANCED_PERMISSION_FIELDS,
        AddressMixin.ADMIN_FIELDSET,
        DATE_FIELDS,
    )
    list_display = ('is_active', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff',)
    list_display_links = ('email', 'first_name', 'last_name',)
    search_fields = ('email', 'first_name', 'last_name',)


admin.site.register(User, EncampUserAdmin)
