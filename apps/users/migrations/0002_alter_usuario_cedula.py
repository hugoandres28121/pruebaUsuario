# Generated by Django 3.2.9 on 2021-11-14 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cedula',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
