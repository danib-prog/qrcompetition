# Generated by Django 4.0.3 on 2022-03-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcomp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='message',
            field=models.TextField(max_length=280),
        ),
    ]