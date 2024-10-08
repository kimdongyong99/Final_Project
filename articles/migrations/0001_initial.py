# Generated by Django 4.2 on 2024-10-02 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=300)),
                ("link", models.URLField(max_length=500)),
                ("image_url", models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
