# Generated by Django 4.0.10 on 2024-05-10 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0010_alter_user_verified_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='src.company'),
        ),
    ]