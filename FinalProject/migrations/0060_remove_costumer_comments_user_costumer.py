# Generated by Django 4.0.3 on 2022-03-20 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProject', '0059_costumer_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costumer',
            name='comments',
        ),
        migrations.AddField(
            model_name='user',
            name='costumer',
            field=models.ForeignKey(blank=True, default=2, null=True, on_delete=django.db.models.deletion.CASCADE, to='FinalProject.costumer'),
        ),
    ]
