# Generated by Django 3.2.9 on 2022-01-08 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hombre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talle', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('color', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mujer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talle', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('color', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Niños',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talle', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('color', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
