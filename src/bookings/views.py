import pandas as pd
from django.db.models import Q
from django.shortcuts import render

# rest-framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
# custom imports
from .serializers import BookingsSerializer, BookingsUploadSerializer, ContainerSerializer
from .models import Booking, Container


class BookingsView(viewsets.ModelViewSet):
    """
    for booking a shipment by a customer
    """
    # permission_classes = (IsAuthenticated, )
    queryset = Booking.objects.all()
    serializer_class = BookingsSerializer

    # def get_queryset(self, request):
    #     edit = self.re
    # quest.is_edit
    #     print(edit)
        # if edit == "True":
        #     return self.queryset.filter(is_edit=edit)
        # else:
        #     return self.queryset.filter(is_edit=edit)

    def list(self, request):
        if not request.user.is_admin:
            # print(request.user.is_admin)
            if request.GET.get('is_edit'):
                edit = request.GET.get('is_edit', None)
                self.queryset = self.queryset.filter(user=request.user, is_edit=edit)
                # self.queryset = self.queryset.filter(Q(user=request.user) |
                #                                      Q(is_edit=edit))
            else:
                self.queryset = self.queryset.filter(user=request.user)

        return super(BookingsView, self).list(request)

    def create(self, request, *args, **kwargs):
        """
        bookings should be a list of dict
        """
        msg = ""
        success = ""
        data = ""
        d = []
        try:
            for data in request.data:
                if data['booking_no'] in [None, ""]:
                    msg = "please enter booking no"
                    success = False
                    data = ""
                    r = {
                        'data': data,
                        'msg': msg,
                        'success': success
                    }
                    d.append(r)
                else:
                    data['user'] = request.user.id
                    success = True
                    serializer = self.get_serializer(data=data)
                    serializer.is_valid(raise_exception=True)
                    self.perform_create(serializer)
                    data = serializer.data
                    # d.append(data)
                    # print(data)
                    msg = "SUCCESSFULLY CREATED"
                    r = {
                        'data': data,
                        'msg': msg,
                        'success': success
                    }
                    d.append(r)

        except Exception as e:
            msg = "exception:", e
            return Response({
                'msg': msg
            })
        return Response({
            'data': d
        })

        # return Response({
        #     'success': success,
        #     'msg': msg,
        #     'data': data
        # })
        """
        the below code also works
        """
        # for data in request.data:
        #     data['user'] = request.user.id
        # serializer = self.get_serializer(data=request.data, many=True)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'success': True,
            'msg': 'Field successfully updated'
        })


class ContainersView(viewsets.ModelViewSet):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer

    def create(self, request, *args, **kwargs):
        """
        containers is a list of dict
        """
        msg = ""
        try:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            msg = "SUCCESS"
        except Exception as e:
            msg = "EXCEPTION"

        return Response({
            'data': serializer.data,
            'success': True,
            'msg': msg
        })


class BookingsUploadView(viewsets.ViewSet):
    serializer_class = BookingsUploadSerializer
    # print(serializer_class.data)
    # parser_classes = (FileUploadParser,)
    # parser_classes = (MultiPartParser, FormParser)

    # @staticmethod
    def create(self, request):
        # print(request.Files['BookingsUploadSerializer'])
        print()
        print(request.data)
        try:
            df = pd.read_csv(request.data['bookings_file'])  # it will be a csv file
            df = df.fillna('')

            msg = "upload-booking"
            for index, value in df.iterrows():
                try:
                    new_booking = Booking()
                    new_booking.user = request.user
                    ################################
                    if value.booking_no in ['', '-']:
                        new_booking.booking_no = '0'
                    else:
                        new_booking.booking_no = value.booking_no
                    ###############################
                    if value.container_no == '':
                        new_booking.container_no = "please enter value"
                    else:
                        new_booking.container_no = value.container_no
                    ###################################
                    if value.vessel_name in ['', '-']:
                        new_booking.vessel_name = "please enter value"
                    else:
                        new_booking.vessel_name = value.vessel_name
                    #######################################
                    if value.pod in ['', '-']:
                        new_booking.pod = "please enter value"
                    else:
                        new_booking.pod = value.pod
                    #######################################
                    if value.pol in ['', '-']:
                        new_booking.pol = "please enter value"
                    else:
                        new_booking.pol = value.pol
                    ###############################
                    if value.shipping_bill_no in ['', '-']:
                        new_booking.shipping_bill_no = "please enter value"
                    else:
                        new_booking.shipping_bill_no = value.shipping_bill_no
                    ###############################
                    if value.shipment_desc in ['', '-']:
                        new_booking.shipment_desc = "please enter value"
                    else:
                        new_booking.shipment_desc = value.shipment_desc
                    ############################
                    if value.seal_no in ['', '-']:
                        new_booking.seal_no = "please enter value"
                    else:
                        new_booking.seal_no = value.seal_no
                    #####################################
                    if value.gross_weight in ['', '-']:
                        new_booking.gross_weight = "please enter value"
                    else:
                        new_booking.gross_weight = value.gross_weight
                    ##############################
                    if value.net_weight in ['', '-']:
                        new_booking.net_weight = "please enter value"
                    else:
                        new_booking.net_weight = value.net_weight
                    ########################################
                    if value.no_of_cartons in ['', '-']:
                        new_booking.no_of_cartons = '0'
                    else:
                        new_booking.no_of_cartons = value.no_of_cartons
                    ###################
                    if value.package_type in ['','-']:
                        new_booking.package_type = "please enter value"
                    else:
                        new_booking.package_type = value.package_type
                    ############################
                    if value.hscode in ['', '-']:
                        new_booking.hscode = None
                    else:
                        new_booking.hscode = value.hscode
                    ######################################
                    if value.move_type in ['', '-']:
                        new_booking.move_type = "please enter value"
                    else:
                        new_booking.move_type = value.move_type
                    if value.freight in ['', '-']:
                        new_booking.freight = "please enter value"
                    else:
                        new_booking.freight = value.freight
                    if value.discharge_type in ['', '-']:
                        new_booking.discharge_type = "please enter value"
                    else:
                        new_booking.discharge_type = value.discharge_type
                    # SHIPPER
                    if value.shipper_addr in ['', '-']:
                        new_booking.shipper_addr = "please enter value"
                    else:
                        new_booking.shipper_addr = value.shipper_addr
                    if value.shipper_country in ['', '-']:
                        new_booking.shipper_country = "please enter value"
                    else:
                        new_booking.shipper_country = value.shipper_country
                    if value.shipper_cust_id in ['', '-']:
                        new_booking.shipper_cust_id = "please enter value"
                    else:
                        new_booking.shipper_cust_id = value.shipper_cust_id
                    # FREIGHT-FORWARDER
                    if value.freight_addr in ['', '-']:
                        new_booking.freight_addr = "please enter value"
                    else:
                        new_booking.freight_addr = value.freight_addr
                    if value.freight_country in ['', '-']:
                        new_booking.freight_country = "please enter value"
                    else:
                        new_booking.freight_country = value.freight_country
                    if value.freight_cust_id in ['','-']:
                        new_booking.freight_cust_id = "please enter value"
                    else:
                        new_booking.freight_cust_id = value.freight_cust_id
                    # CONSIGNEE
                    if value.consign_addr in ['', '-']:
                        new_booking.consign_addr = "please enter value"
                    else:
                        new_booking.consign_addr = value.consign_addr
                    if value.consign_country in ['', '-']:
                        new_booking.consign_country = "please enter value"
                    else:
                        new_booking.consign_country = value.consign_country
                    if value.consign_cust_id in ['', '-']:
                        new_booking.consign_cust_id = "please enter value"
                    else:
                        new_booking.consign_cust_id = value.consign_cust_id
                    # NOTIFY 1
                    if value.notify1_addr in ['', '-']:
                        new_booking.notify1_addr = "please enter value"
                    else:
                        new_booking.notify1_addr = value.notify1_addr
                    if value.notify1_country in ['', '-']:
                        new_booking.notify1_country = "please enter value"
                    else:
                        new_booking.notify1_country = value.notify1_country
                    if value.notify1_cust_id in ['', '-']:
                        new_booking.notify1_cust_id = "please enter value"
                    else:
                        new_booking.notify1_cust_id = value.notify1_cust_id
                    #########################
                    if value.notify2_addr in ['', '-']:
                        new_booking.notify2_addr = "please enter value"
                    else:
                        new_booking.notify2_addr = value.notify2_addr
                    if value.notify2_country in ['', '-']:
                        new_booking.notify2_country = "please enter value"
                    else:
                        new_booking.notify2_country = value.notify2_country
                    if value.notify2_cust_id in ['', '-']:
                        new_booking.notify2_cust_id = "please enter value"
                    else:
                        new_booking.notify2_cust_id = value.notify2_cust_id
                    #########################
                    new_booking.save()
                    success = True
                    msg = "BOOKING SUCCESSFUL"

                except Exception as e:
                    msg = (str(e))
                    success = False

        except IOError as e:
            msg = (str(e))
            success = False

        return Response({
            'msg': msg,
            'success': success
            })






