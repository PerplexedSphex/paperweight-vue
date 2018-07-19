from rest_framework import serializers

from .models import User, AccountHolder


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='user-detail', lookup_field='uuid'
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'street_address', 'city', 'state', 'zip_code',
            'full_address_raw', 'account_holder', 'uuid', 'url',
        )
