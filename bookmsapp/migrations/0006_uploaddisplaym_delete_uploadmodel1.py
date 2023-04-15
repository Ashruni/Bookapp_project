# Generated by Django 4.1 on 2023-03-07 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmsapp', '0005_alter_uploadmodel1_bookdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploaddisplaym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=40)),
                ('bookpdf', models.FileField(upload_to='bookmsapp/static')),
                ('uploaddate', models.DateTimeField(auto_now_add=True)),
                ('bookimage', models.FileField(upload_to='bookmsapp/static')),
                ('bookauthor', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='uploadmodel1',
        ),
    ]
