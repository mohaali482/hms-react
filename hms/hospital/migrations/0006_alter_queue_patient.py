# Generated by Django 3.2.9 on 2022-01-15 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_queue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='hospital.patient', verbose_name='Patient'),
        ),
    ]