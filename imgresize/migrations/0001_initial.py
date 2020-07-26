# Generated by Django 3.0.8 on 2020-07-26 10:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='img/')),
                ('width', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('height', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]