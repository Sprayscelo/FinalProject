# Generated by Django 4.0 on 2021-12-20 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProject', '0006_equipments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
