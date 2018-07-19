from core.viewsets import TenantModelViewSet
from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(TenantModelViewSet):
    model = Person
    serializer_class = PersonSerializer
    lookup_field = 'uuid'
