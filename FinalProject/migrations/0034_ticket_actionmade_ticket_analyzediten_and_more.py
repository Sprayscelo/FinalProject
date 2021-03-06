# Generated by Django 4.0 on 2022-01-06 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProject', '0033_alter_costumer_priority_alter_ticket_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='actionMade',
            field=models.CharField(choices=[('Costumer instruction', 'Costumer Instruction'), ('Register/Update', 'Register/Update'), ('Validation/Reports', 'Validation/Reports'), ('Veichle unlock', 'Veichle unlock'), ('Escaled', 'Escaled'), ('Reset', 'Reset'), ('Internal procedure', 'internal procedure')], default='', max_length=255),
        ),
        migrations.AddField(
            model_name='ticket',
            name='analyzedIten',
            field=models.CharField(choices=[('Antenna - GPS', 'Antenna - GSM'), ('Antena - GSM', 'Antena - GSM'), ('CAN', 'CAN'), ('Sim Card', 'Sim card'), ('Equipment', 'Equipment'), ('Speed Sensor', 'Speed Sensor'), ('Rpm Sensor', 'Rpm Sensor')], default='', max_length=255),
        ),
        migrations.AddField(
            model_name='ticket',
            name='plataform',
            field=models.CharField(choices=[('App Wikidados', 'App Wikidados'), ('Dynamix', 'Fleet Manager'), ('Gconnect', 'GConnect'), ('Getrak', 'Getrak'), ('Vdoweb', 'Vdoweb'), ('CRM', 'CRM'), ('Passanger', 'Passanger')], default='', max_length=255),
        ),
        migrations.AddField(
            model_name='ticket',
            name='solution',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='costumer',
            name='priority',
            field=models.CharField(choices=[('Low', 1), ('Medium', 2), ('High', 3), ('Urgent', 4)], max_length=255),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.CharField(choices=[('Low', 1), ('Medium', 2), ('High', 3), ('Urgent', 4)], max_length=255),
        ),
    ]
