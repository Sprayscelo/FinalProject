# Generated by Django 4.0 on 2022-01-02 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProject', '0017_alter_serviceorder_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Smart', 'Smart'), ('Premium', 'Premium'), ('Essential', 'Essential'), ('Video managment', 'Video managment'), ('Evolution', 'Evolution'), ('Silometria', 'Silometria'), ('OnBoard', 'OnBoard')], max_length=254)),
                ('serialNumber', models.CharField(max_length=30)),
                ('phoneOperator', models.CharField(choices=[('ALG', 'Algar'), ('VIV', 'Vivo'), ('OI', 'OI'), ('CLR', 'Claro'), ('TIM', 'Tim')], max_length=30)),
                ('chip', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('ATV', 'Active'), ('EXC', 'Execution'), ('STK', 'Stock'), ('WRT', 'Warrantly'), ('OUS', 'Out of Service'), ('DSB', 'Disabled')], max_length=30)),
                ('inUseDate', models.DateTimeField(blank=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinalProject.product')),
            ],
        ),
        migrations.AlterField(
            model_name='costumer',
            name='type',
            field=models.CharField(choices=[('Company Costumer', 'Company Costumer'), ('Physical Costumer', 'Physical Costumer')], max_length=255),
        ),
        migrations.DeleteModel(
            name='Equipments',
        ),
    ]
