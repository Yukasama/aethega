# Generated by Django 4.0.4 on 2022-06-22 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eye', '0018_remove_financial_roe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='symbol',
            field=models.SlugField(max_length=10),
        ),
    ]
