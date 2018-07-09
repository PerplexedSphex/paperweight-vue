from django.db import models
from authtools.models import AbstractNamedUser


class EncampUser(AbstractNamedUser):
    """Creating this now so it's easier to customize later without borking the db"""
    pass
