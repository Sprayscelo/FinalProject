# Generated by Django 4.0 on 2022-01-11 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProject', '0050_alter_costumer_cnpj_alter_costumer_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='priority',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], max_length=255),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')]),
        ),
    ]
