# Generated by Django 4.0 on 2021-12-30 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProject', '0009_alter_ticket_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='comment',
            field=models.JSONField(),
        ),
    ]
