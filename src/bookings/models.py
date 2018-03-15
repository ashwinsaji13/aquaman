from django.db import models
from model_utils.fields import StatusField
from model_utils import Choices
from src.accounts.models import Account
# Create your models here.


class Booking(models.Model):
    """

    """
    MOVE_TYPE = Choices('CY',)
    FREIGHT = Choices('Prepaid', 'Collect')
    DISCHARGE_TYPE = Choices('FCL',)

    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    booking_no = models.IntegerField()
    container_no = models.CharField(max_length=32)
    vessel_name = models.CharField(max_length=32)
    pod = models.CharField(max_length=32)
    pol = models.CharField(max_length=32)
    shipping_bill_no = models.CharField(max_length=32)
    shipment_desc = models.CharField(max_length=128)
    seal_no = models.CharField(max_length=32)
    gross_weight = models.CharField(max_length=64)
    net_weight = models.CharField(max_length=64)
    no_of_cartons = models.IntegerField()
    package_type = models.CharField(max_length=64)
    hscode = models.IntegerField()
    move_type = StatusField(choices_name='MOVE_TYPE', default=MOVE_TYPE.CY)
    freight = StatusField(choices_name='FREIGHT', default=FREIGHT.Prepaid)
    discharge_type = StatusField(choices_name='DISCHARGE_TYPE', default=DISCHARGE_TYPE.FCL)
    # SHIPPER
    shipper_addr = models.CharField(max_length=256)
    shipper_country = models.CharField(max_length=256)
    shipper_cust_id = models.CharField(max_length=64)
    # FREIGHT-FORWARDER
    freight_addr = models.CharField(max_length=256)
    freight_country = models.CharField(max_length=256)
    freight_cust_id = models.CharField(max_length=64)
    # CONSIGNEE
    consign_addr = models.CharField(max_length=256)
    consign_country = models.CharField(max_length=256)
    consign_cust_id = models.CharField(max_length=64)
    # NOTIFY 1
    notify1_addr = models.CharField(max_length=256)
    notify1_country = models.CharField(max_length=256)
    notify1_cust_id = models.CharField(max_length=64)
    # NOTIFY 2
    notify2_addr = models.CharField(max_length=256)
    notify2_country = models.CharField(max_length=256)
    notify2_cust_id = models.CharField(max_length=64)
    # for making the forms editable
    # edit = models.BooleanField(default=True)

    def __str__(self):
        return self.shipper_cust_id

