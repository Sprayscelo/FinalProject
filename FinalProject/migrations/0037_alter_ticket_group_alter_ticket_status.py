# Generated by Django 4.0 on 2022-01-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProject', '0036_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='group',
            field=models.CharField(choices=[('Support', 'Support'), ('Financial', 'Financial'), ('Commercial', 'Commercial'), ('Services', 'Services'), ('Administrative', 'Administrative'), ('Legal', 'Legal'), ('Stock and Supplies', 'Stock and Supplies'), ('Development', 'Development'), ('Costumer Success', 'Costumer Success')], default='Support', max_length=255),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Waiting for response', 'Waiting for response'), ('Escaled', 'Escaled'), ('Closed', 'Closed')], default='', max_length=255),
        ),
    ]