# Generated by Django 4.0.5 on 2022-06-28 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eye', '0025_remove_info_sharesoutstanding_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='forwardEPS',
            new_name='forwardEps',
        ),
    ]
