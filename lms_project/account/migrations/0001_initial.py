# Generated by Django 5.0.7 on 2024-08-15 06:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountLoginType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginType', models.CharField(choices=[('NORMAL', 'Normal'), ('GOOGLE', 'Google')], default='NORMAL', max_length=10)),
            ],
            options={
                'db_table': 'account_login_type',
            },
        ),
        migrations.CreateModel(
            name='GoogleProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'db_table': 'googleprofile',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=64, unique=True)),
                ('password', models.CharField(default='n', max_length=64)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('loginType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.accountlogintype')),
            ],
            options={
                'db_table': 'account',
            },
        ),
    ]
