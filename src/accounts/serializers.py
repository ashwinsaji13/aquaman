# rest-framework
from rest_framework import serializers
# custom imports
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account

        write_only_fields = ['password']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['active', 'admin', 'staff', 'superuser']
        fields = ['id', 'email', 'full_name', 'phone_number', 'address'] + \
            write_only_fields + read_only_fields
