# Generated by Django 3.2.9 on 2022-01-15 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_rename_conditons_patienthistory_conditions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='History Date'),
        ),
    ]