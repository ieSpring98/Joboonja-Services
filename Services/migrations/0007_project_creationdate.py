# Generated by Django 2.0.7 on 2019-04-15 17:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0006_auto_20190209_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='creationDate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
