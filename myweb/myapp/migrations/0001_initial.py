# Generated by Django 4.1 on 2023-05-08 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
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
                ("userName", models.CharField(max_length=10)),
                ("userId", models.CharField(max_length=10)),
                ("userPw", models.CharField(max_length=20)),
            ],
        ),
    ]
