from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class DefaultsMixin:
    """Default settings for view authentication, permissions,
    filtering and pagination."""
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class EncampModelViewSet(DefaultsMixin, ModelViewSet):
    """An ABSTRACT class, which other model viewsets should inherit from"""
    model = None  # model must inherit from TenantMixin

    def get_queryset(self):
        return self.model.objects.of_requester(self.request)

    def create(self, request, *args, **kwargs):
        request.data = dict(request.data)
        request.data['record_owner'] = request.user.account_holder.id
        return super().create(request, *args, **kwargs)
