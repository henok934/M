# Generated by Django 5.1 on 2024-10-07 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin',
            options={},
        ),
        migrations.AlterModelManagers(
            name='admin',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='admin',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='admin',
            name='gender',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='admin',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
