# Generated by Django 4.0.4 on 2022-05-24 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_register1_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientname', models.CharField(max_length=100)),
                ('clienturl', models.CharField(max_length=500)),
            ],
        ),
    ]
