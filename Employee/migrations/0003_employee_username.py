# Generated by Django 4.1.7 on 2023-05-31 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0002_employee_user_username_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(default='employee', max_length=255, unique=True),
        ),
          migrations.AlterField(
        model_name='employee',
        name='username',
        field=models.CharField(max_length=255, unique=True, default='employee'),
        ),
    ]
