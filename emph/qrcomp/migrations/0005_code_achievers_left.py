# Generated by Django 4.0.3 on 2022-03-21 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcomp', '0004_code_name_human_readable'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='achievers_left',
            field=models.IntegerField(default=5),
        ),
    ]
