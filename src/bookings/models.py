from django.db import models
from model_utils.fields import StatusField
from model_utils import Choices
from src.accounts.models import Account
# Create your models here.


class Booking(models.Model):
    """
    Bookings Model for container booking
    """
    # MOVE_TYPE = Choices('CY',)
    # FREIGHT = Choices('Prepaid', 'Collect')
    # DISCHARGE_TYPE = Choices('FCL',)

    user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True)
    booking_no = models.IntegerField(null=True, blank=True)
    # container_no = models.CharField(max_length=32, null=True, blank=True)
    vessel_name = models.CharField(max_length=32, null=True, blank=True)
    pod = models.CharField(max_length=32, null=True, blank=True)
    pol = models.CharField(max_length=32, null=True, blank=True)
    shipping_bill_no = models.CharField(max_length=32, null=True, blank=True)
    shipment_desc = models.TextField(null=True, blank=True)
    seal_no = models.CharField(max_length=32, null=True, blank=True)
    # VOYAGE
    voyage = models.CharField(max_length=64, null=True, blank=True)
    # FINAL DESTINATION
    final_dest = models.CharField(max_length=64, null=True, blank=True)
    # PLACE OF RECEIPT
    p_o_r = models.CharField(max_length=64, null=True, blank=True)
    # package_type = models.CharField(max_length=64, null=True, blank=True)
    hscode = models.IntegerField(null=True, blank=True)
    # GST
    gst = models.CharField(max_length=32, null=True, blank=True)
    # IMPORT/EXPORT CODE
    iec = models.CharField(max_length=64, null=True, blank=True)
    #  EMAIL ID
    email_id = models.EmailField(null=True, blank=True)
    # move_type = StatusField(choices_name='MOVE_TYPE', default=MOVE_TYPE.CY)
    # freight = StatusField(choices_name='FREIGHT', default=FREIGHT.Prepaid)
    # discharge_type = StatusField(choices_name='DISCHARGE_TYPE', default=DISCHARGE_TYPE.FCL)
    move_type = models.CharField(max_length=32, null=True, blank=True)
    freight = models.CharField(max_length=32, null=True, blank=True)
    discharge_type = models.CharField(max_length=32, null=True, blank=True)
    # SHIPPER
    shipper_addr = models.CharField(max_length=256, null=True, blank=True)
    shipper_country = models.CharField(max_length=256, null=True, blank=True)
    shipper_cust_id = models.CharField(max_length=64, null=True, blank=True)
    # FREIGHT-FORWARDER
    freight_addr = models.CharField(max_length=256, null=True, blank=True)
    freight_country = models.CharField(max_length=256, null=True, blank=True)
    freight_cust_id = models.CharField(max_length=64, null=True, blank=True)
    # CONSIGNEE
    consign_addr = models.CharField(max_length=256, null=True, blank=True)
    consign_country = models.CharField(max_length=256, null=True, blank=True)
    consign_cust_id = models.CharField(max_length=64, null=True, blank=True)
    # NOTIFY 1
    notify1_addr = models.CharField(max_length=256, null=True, blank=True)
    notify1_country = models.CharField(max_length=256, null=True, blank=True)
    notify1_cust_id = models.CharField(max_length=64, null=True, blank=True)
    # NOTIFY 2
    notify2_addr = models.CharField(max_length=256, null=True, blank=True)
    notify2_country = models.CharField(max_length=256, null=True, blank=True)
    notify2_cust_id = models.CharField(max_length=64, null=True, blank=True)
    # for making the forms editable
    is_edit = models.BooleanField(default=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return "Booking-No:{0}".format(self.booking_no)

    # @property
    # def is_edit(self):
    #     return self.is_edit


class Container(models.Model):
    booking = models.ForeignKey(Booking, related_name="container_booking", on_delete=models.CASCADE)
    container_no = models.CharField(max_length=32, null=True, blank=True)
    gross_weight = models.CharField(max_length=64, null=True, blank=True)
    net_weight = models.CharField(max_length=64, null=True, blank=True)
    no_of_cartons = models.IntegerField(null=True, blank=True)
    package_type = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.container_no

