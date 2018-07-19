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
        if request.user.account_holder:
            return self.owned_by(request.user.account_holder)
        else:
            return self.none()
