# Generated by Django 4.0 on 2021-12-17 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProject', '0005_serviceorder_relatedticket_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('SMT', 'Smart'), ('PRM', 'Premium'), ('ESS', 'Essential'), ('VMG', 'Video managment'), ('EVO', 'Evolution'), ('SLM', 'Silometria'), ('VDO', 'OnBoard')], max_length=254)),
                ('serialNumber', models.CharField(max_length=30)),
                ('phoneOperator', models.CharField(choices=[('ALG', 'Algar'), ('VIV', 'Vivo'), ('OI', 'OI'), ('CLR', 'Claro'), ('TIM', 'Tim')], max_length=30)),
                ('chip', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('ATV', 'Active'), ('EXC', 'Execution'), ('STK', 'Stock'), ('WRT', 'Warrantly'), ('OUS', 'Out of Service'), ('DSB', 'Disabled')], max_length=30)),
                ('inUseDate', models.DateTimeField(blank=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinalProject.product')),
            ],
        ),
    ]