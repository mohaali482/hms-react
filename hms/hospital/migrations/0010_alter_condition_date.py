# Generated by Django 3.2.9 on 2022-01-15 23:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0009_alter_condition_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='History Date'),
        ),
    ]
