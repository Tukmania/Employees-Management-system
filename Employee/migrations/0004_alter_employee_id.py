# Generated by Django 4.1.7 on 2023-06-04 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_employee_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
