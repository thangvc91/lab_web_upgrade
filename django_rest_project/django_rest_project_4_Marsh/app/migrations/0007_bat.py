# Generated by Django 4.0.4 on 2022-06-11 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_staffurl_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batpassword', models.CharField(max_length=20)),
                ('batuser', models.CharField(max_length=50)),
                ('batemail', models.CharField(max_length=50)),
                ('batrelationship', models.CharField(max_length=50, null=True)),
                ('batdob', models.CharField(max_length=50, null=True)),
                ('batgender', models.CharField(max_length=10, null=True)),
                ('batid', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
