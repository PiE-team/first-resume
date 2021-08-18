# Generated by Django 3.2.5 on 2021-08-02 11:10

import BackPyRating.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clint_name', models.CharField(max_length=150)),
                ('rating', models.CharField(choices=[('★★★★★', 'five_star'), ('★★★★', 'four_star'), ('★★★', 'three_star'), ('★★', 'two_star'), ('★', 'one_star')], max_length=150)),
                ('comment', models.TextField()),
                ('position', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to=BackPyRating.models.upload_image_path)),
            ],
        ),
    ]