# Generated by Django 4.1.5 on 2023-02-01 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_drink_drinks_drink_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='available',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='cuisine',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='item_id',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='price',
        ),
    ]