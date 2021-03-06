# Generated by Django 3.2.5 on 2021-07-24 10:46

import BackPyTeam.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('position', models.CharField(max_length=80)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=BackPyTeam.models.upload_image_path)),
            ],
        ),
    ]
