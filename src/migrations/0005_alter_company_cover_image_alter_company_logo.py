# Generated by Django 4.0.10 on 2024-05-09 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='cover_image',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.TextField(null=True),
        ),
    ]