# Generated by Django 4.0 on 2022-01-08 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProject', '0034_ticket_actionmade_ticket_analyzediten_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='group',
            field=models.CharField(choices=[('Support', 'Support'), ('Financial', 'Financial'), ('Commercial', 'Commercial'), ('Services', 'Services'), ('Administrative', 'Administrative'), ('Legal', 'Legal'), ('Stock and Supplies', 'Stock and Supplies'), ('Development', 'Development'), ('Costumer Success', 'Costumer Success')], default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='actionMade',
            field=models.CharField(choices=[('Costumer instruction', 'Costumer Instruction'), ('Register/Update', 'Register/Update'), ('Validation/Reports', 'Validation/Reports'), ('Veichle unlock', 'Veichle unlock'), ('Escaled', 'Escaled'), ('Reset', 'Reset'), ('Internal procedure', 'Internal procedure')], default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Waiting for response', 'Waiting for response'), ('Escaled', 'Escaled'), ('Closed', 'Closed')], default='', max_length=255),
        ),
    ]