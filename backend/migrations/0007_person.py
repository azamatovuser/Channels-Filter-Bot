# Generated by Django 4.2 on 2023-04-13 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.CharField(max_length=221, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=221)),
            ],
        ),
    ]
