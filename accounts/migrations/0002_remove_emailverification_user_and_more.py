# Generated by Django 4.2 on 2024-10-08 10:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="emailverification",
            name="user",
        ),
        migrations.AddField(
            model_name="emailverification",
            name="email",
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
    ]
