# Generated by Django 3.1.7 on 2021-03-23 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20210322_1116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['timestamp']},
        ),
    ]
