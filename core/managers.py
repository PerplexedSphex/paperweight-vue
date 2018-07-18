from django.db import models


class EncampBaseModelManager(models.Manager):

    def owned_by(self, owner):
        """Get records owned by specific owner

        Params:
        owner -- the record owner, an AccountHolder object
        """
        return super().get_queryset().filter(record_owner=owner)

    def of_requester(self, request):
        """Get records owned by the requester

        Params:
        request -- django request
        """
        if request.user.is_authenticated:
            # if request.user.has_perm()
            return self.owned_by(request.user.account_holder)
        else:
            # todo - figure out how to check if an object requires no permission to view
            return self.none()
