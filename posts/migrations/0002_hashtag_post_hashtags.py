# Generated by Django 4.2 on 2024-09-27 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hashtag",
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
                ("content", models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="hashtags",
            field=models.ManyToManyField(
                blank=True, related_name="article_hashtags", to="posts.hashtag"
            ),
        ),
    ]
