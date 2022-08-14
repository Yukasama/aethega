# Generated by Django 4.0.6 on 2022-08-12 15:01

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(default='Guest', max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('biography', models.TextField(default='My interesting Biography...')),
                ('profile_image', models.ImageField(blank=True, default=account.models.get_profile_image_default, null=True, upload_to=account.models.get_profile_image_filepath)),
                ('email_verified', models.BooleanField(default=False)),
                ('two_factor_auth', models.CharField(blank=True, choices=[('Email', 'Email'), ('SMS', 'SMS'), ('Google Auth', 'Google Authenticator')], default=None, max_length=20, null=True)),
                ('two_factor_key', models.CharField(blank=True, max_length=10, null=True)),
                ('hide_email', models.BooleanField(default=True)),
                ('profile_private', models.BooleanField(default=False)),
                ('show_investments', models.BooleanField(default=False)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('last_login', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
