# Generated by Django 3.2.5 on 2021-07-06 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='something',
            name='some_image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
