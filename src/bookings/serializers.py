# rest-framework
from rest_framework import serializers
# custom imports
from .models import Booking


class BookingsSerializer(serializers.ModelSerializer):
    """
    this serializr is for booking a shipment
    """
    class Meta:
        model = Booking
        fields = [f.name for f in model._meta.fields]
        # exclude = ('user',)


class BookingsUploadSerializer(serializers.Serializer):

    bookings_file = serializers.FileField(required=True)

    class Meta:
        fields = ['bookings_file']



