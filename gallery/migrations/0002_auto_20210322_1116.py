# Generated by Django 3.1.7 on 2021-03-22 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
