from rest_framework import viewsets

from core.viewsets import EncampModelViewSet
from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(EncampModelViewSet):
    model = Person
    serializer_class = PersonSerializer
