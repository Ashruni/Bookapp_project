# Generated by Django 4.1 on 2023-03-06 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmsapp', '0002_alter_uploadmodel1_bookdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadmodel1',
            name='bookdate',
            field=models.DateField(default='2023-03-06'),
        ),
    ]
