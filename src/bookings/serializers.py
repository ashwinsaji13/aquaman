# rest-framework
from rest_framework import serializers
# custom imports
from .models import Booking, Container


class ContainerSerializer(serializers.ModelSerializer):
    """
    this serializer is for the conatiner related fields
    """
    # book_details = BookingsSerializer(source='booking', read_only=True)

    class Meta:
        model = Container
        # read_only_fields = ['book_details']
        fields = [f.name for f in model._meta.fields]


class BookingsSerializer(serializers.ModelSerializer):
    """
    this serializer is for booking a shipment
    """
    container_details = ContainerSerializer(source='container_booking', many=True, read_only=True)

    class Meta:
        model = Booking
        read_only_fields = ['container_details']
        fields = [f.name for f in model._meta.fields] + read_only_fields

        @staticmethod
        def setup_eager_loading(queryset):
            """
            Performs necessary eager loading of data.
            """
            queryset = queryset.prefetch_related('container_booking')

            return queryset


class BookingsUploadSerializer(serializers.Serializer):

    bookings_file = serializers.FileField(required=True)

    class Meta:
        fields = ['bookings_file']


class TrialPageSerializer(serializers.Serializer):

    trial_file = serializers.FileField(required=True)

    class Meta:
        fields = ['trial_file']






