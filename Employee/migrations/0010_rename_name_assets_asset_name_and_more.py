# Generated by Django 4.2.4 on 2023-08-07 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0009_alter_assets_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assets',
            old_name='name',
            new_name='asset_name',
        ),
        migrations.RenameField(
            model_name='assign',
            old_name='asset',
            new_name='asset_name',
        ),
    ]
