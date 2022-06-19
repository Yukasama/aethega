# Generated by Django 4.0.4 on 2022-06-18 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eye', '0008_financial_eye_financi_year_cf6af2_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='financial',
            name='eye_financi_year_cf6af2_idx',
        ),
        migrations.AddIndex(
            model_name='financial',
            index=models.Index(fields=['symbol'], name='eye_financi_symbol__9fa4f5_idx'),
        ),
    ]
