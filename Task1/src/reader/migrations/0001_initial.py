# Generated by Django 4.2.7 on 2023-11-22 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=70)),
                ('price', models.FloatField()),
                ('color', models.CharField(max_length=15)),
            ],
        ),
    ]