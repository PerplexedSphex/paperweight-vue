from core.viewsets import EncampBaseModelViewSet
from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(EncampBaseModelViewSet):
    model = Person
    serializer_class = PersonSerializer
