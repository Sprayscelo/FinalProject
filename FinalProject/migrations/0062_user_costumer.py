# Generated by Django 4.0.3 on 2022-03-20 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProject', '0061_remove_user_costumer'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='costumer',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='FinalProject.costumer'),
        ),
    ]
