# Generated by Django 3.0.2 on 2020-02-04 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_img', models.FileField(upload_to='')),
                ('hotel_name', models.CharField(max_length=50)),
            ],
        ),
    ]