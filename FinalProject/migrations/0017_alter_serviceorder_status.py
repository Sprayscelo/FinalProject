# Generated by Django 4.0 on 2022-01-02 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProject', '0016_alter_ticket_costumer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceorder',
            name='status',
            field=models.CharField(choices=[('Created', 'Created'), ('Aproved', 'Aproved'), ('Waiting for supply', 'Waiting for supply'), ('Waiting for schedule', 'Waiting for schedule'), ('Scheduled', 'Scheduled'), ('Delivered', 'Delivered'), ('Billed', 'Billed'), ('Warrantly', 'Warrantly'), ('Cancelled', 'Cancelled')], default='', max_length=50),
        ),
    ]
