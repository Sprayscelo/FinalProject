# Generated by Django 4.0 on 2022-01-11 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProject', '0047_remove_costumer_comm_costumer_comments_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='costumer',
            old_name='clientName',
            new_name='name',
        ),
    ]
