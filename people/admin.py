from django.contrib import admin

from .models import Person


class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('record_owner',)


admin.site.register(Person, PersonAdmin)
