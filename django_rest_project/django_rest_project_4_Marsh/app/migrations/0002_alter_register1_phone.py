# Generated by Django 4.0.4 on 2022-05-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register1',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
