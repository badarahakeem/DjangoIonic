# Generated by Django 3.1 on 2020-08-26 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0003_auto_20200826_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ios',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
