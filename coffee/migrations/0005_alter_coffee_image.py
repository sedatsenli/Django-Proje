# Generated by Django 4.1.4 on 2023-01-09 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0004_alter_coffee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='image',
            field=models.ImageField(upload_to='coffee'),
        ),
    ]
