# Generated by Django 5.0.4 on 2024-04-30 16:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\(\\+996\\)\\d{9}$')])),
            ],
        ),
    ]