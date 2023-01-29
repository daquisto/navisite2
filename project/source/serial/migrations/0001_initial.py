# Generated by Django 4.1.4 on 2023-01-18 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guitar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=25)),
                ('serial_number', models.CharField(max_length=15)),
                ('year_of_purchase', models.IntegerField()),
                ('brand_new', models.BooleanField()),
                ('previous_owner', models.CharField(max_length=25)),
                ('current_owner', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to=None)),
                ('further_info', models.TextField()),
            ],
        ),
    ]
