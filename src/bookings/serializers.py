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
        fields = '__all__'
        # exclude = ('user',)


class BookingsUploadSerializer(serializers.Serializer):

    File = serializers.FileField(required=True)

    class Meta:
        fields = ['Bookings_file']



