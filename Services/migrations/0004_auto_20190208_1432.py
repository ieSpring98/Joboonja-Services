# Generated by Django 2.1.5 on 2019-02-08 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0003_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
