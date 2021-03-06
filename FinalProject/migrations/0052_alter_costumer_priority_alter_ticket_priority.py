# Generated by Django 4.0 on 2022-01-11 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProject', '0051_alter_costumer_priority_alter_ticket_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='priority',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('4', '3'), ('4', '4')], default=1),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('4', '3'), ('4', '4')]),
        ),
    ]
