# Generated by Django 2.0.2 on 2018-03-06 09:21

from django.db import migrations, models
import src.accounts.managers


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180304_1818'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('objects', src.accounts.managers.AccountManager()),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='superuser',
            field=models.BooleanField(default=False),
        ),
    ]
