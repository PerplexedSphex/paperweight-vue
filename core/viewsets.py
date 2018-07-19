from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class EncampBaseModelViewSet(ModelViewSet):
    """An ABSTRACT class, which other model viewsets should inherit from"""
    model = None  # model should inherit from EncampBaseModel

    def get_queryset(self):
        return self.model.objects.of_requester(self.request)

    def perform_create(self, serializer):
        record_owner = self.request.user.account_holder
        assert record_owner, (
            'Cannot create object as the User is not associated with'
            'an AccountHolder.'
        )
        serializer.save(record_owner=record_owner)

    # Default settings for view authentication, permissions, pagination, lookup field
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100

    lookup_field = 'uuid'
