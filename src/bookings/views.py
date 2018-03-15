from django.shortcuts import render

# rest-framework
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
# custom imports
from .serializers import BookingsSerializer
from .models import Booking


class BookingsView(viewsets.ModelViewSet):
    """
    for booking a shipment by a customer
    """
    # permission_classes = []
    queryset = Booking.objects.all()
    serializer_class = BookingsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'success': True,
            'status': status.HTTP_201_CREATED,
            'data': serializer.data
        })

    # def partial_update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return self.update(request, *args, **kwargs)



