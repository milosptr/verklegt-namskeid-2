# Generated by Django 4.0.10 on 2024-05-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0008_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(default=0),
        ),
    ]