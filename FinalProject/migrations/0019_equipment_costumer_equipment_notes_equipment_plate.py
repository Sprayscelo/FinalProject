# Generated by Django 4.0 on 2022-01-02 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProject', '0018_equipment_alter_costumer_type_delete_equipments'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='costumer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='FinalProject.costumer'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='notes',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='equipment',
            name='plate',
            field=models.CharField(default='', max_length=8),
        ),
    ]
