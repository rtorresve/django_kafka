from rest_framework import serializers

from . import models


class PersonSerializer(serializers.ModelSerializer):
    MESSAGE_TYPE = 'person'
    VERSION = 1
    KEY_FIELD = 'uuid'

    class Meta:
        model = models.Person
        fields = ['uuid', 'first_name', 'last_name']
