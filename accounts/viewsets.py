from rest_framework.viewsets import ModelViewSet

from core.viewsets import DefaultsMixin
from .models import User, AccountHolder
from .serializers import UserSerializer


class UserViewSet(DefaultsMixin, ModelViewSet):
    model = User
    serializer_class = UserSerializer
    lookup_field = 'uuid'

    def get_queryset(self):
        if self.request.user.account_holder:
            return self.request.user.account_holder.user_set.all()
        elif self.request.user.is_authenticated:
            return User.objects.get(id=self.request.user.id)
        else:
            return User.objects.none()
