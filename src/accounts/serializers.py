# rest-framework
from rest_framework import serializers
# custom imports
from .models import *


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account

        read_only_fields = ['email', 'full_name', 'phone_number', 'address', 'active', 'admin', 'staff', 'superuser']
        write_only_fields = ['password']

        fields = read_only_fields + write_only_fields

        extra_kwargs = {
            'password': {'write_only': True}
        }



