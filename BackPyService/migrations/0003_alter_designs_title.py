# Generated by Django 3.2.2 on 2021-07-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackPyService', '0002_auto_20210722_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designs',
            name='title',
            field=models.CharField(choices=[('xxxx', 'UI'), ('UX', 'UX')], max_length=50),
        ),
    ]
