from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='person-detail', lookup_field='uuid')
    record_owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='uuid',
    )

    class Meta:
        model = Person
        fields = (
            'first_name', 'last_name', 'email',
            'street_address', 'city', 'state', 'zip_code',
            'full_address_raw', 'record_owner', 'uuid', 'url',
        )
