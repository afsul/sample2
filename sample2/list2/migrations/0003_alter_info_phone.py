# Generated by Django 4.0.2 on 2022-02-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list2', '0002_info_email_info_name_info_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='phone',
            field=models.IntegerField(editable=False),
        ),
    ]
