# Generated by Django 2.0.2 on 2018-04-03 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_auto_20180308_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_edit',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='consign_addr',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='consign_country',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='consign_cust_id',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='container_no',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='freight_addr',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='freight_country',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='freight_cust_id',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='gross_weight',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='hscode',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='net_weight',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='no_of_cartons',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='notify1_addr',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='notify1_country',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='notify1_cust_id',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='notify2_addr',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='notify2_country',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='notify2_cust_id',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='package_type',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='pod',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='pol',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='seal_no',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='shipment_desc',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='shipper_addr',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='shipper_country',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='shipper_cust_id',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='shipping_bill_no',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='vessel_name',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
