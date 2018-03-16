# rest-framework
from rest_framework import serializers
# custom imports
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account

        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['id', 'email', 'full_name', 'phone_number', 'address', 'active', 'admin', 'staff', 'superuser']
