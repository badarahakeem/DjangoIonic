# Generated by Django 3.1 on 2020-08-26 14:35

import backoffice.userManager
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('reference', models.CharField(db_index=True, max_length=100)),
                ('qrCode', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d')),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('available', models.BooleanField(default=True)),
                ('valid', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Bike',
                'verbose_name_plural': 'Bikes',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('facebookId', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('android', models.BooleanField(blank=True, default=False)),
                ('ios', models.NullBooleanField(default=False)),
                ('acceptPush', models.BooleanField(default=False)),
                ('pushToken', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('valid', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', backoffice.userManager.UserManager()),
            ],
        ),
    ]