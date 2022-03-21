# Generated by Django 4.0.3 on 2022-03-19 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('message', models.CharField(max_length=280)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qrcomp.code')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qrcomp.player')),
            ],
        ),
    ]