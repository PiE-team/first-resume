# Generated by Django 3.2.2 on 2021-07-24 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackPyService', '0013_alter_service_icons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icons',
            field=models.CharField(choices=[('ti-wand', 'Clean Code (magic wand)'), ('ti-comments-smiley', 'DEDICATED SUPPORT (smile comment)'), ('ti-heart', 'USER FRIENDLY (heart)'), ('ti-palette', 'MODERN DESIGN'), ('ti-headphone-alt', 'FAST SUPPORT (headphone)'), ('ti-light-bulb', 'EXCELLENT IDEAS (bulb lamp)')], default='ti-wand', max_length=30),
        ),
    ]
