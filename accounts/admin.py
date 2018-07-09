from django.contrib import admin
from authtools.admin import UserAdmin

from .models import EncampUser

admin.site.register(EncampUser, UserAdmin)
