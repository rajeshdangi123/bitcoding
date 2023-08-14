# Generated by Django 4.2.4 on 2023-08-12 10:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bom",
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
                (
                    "part_number",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("quantity", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Disti",
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
                (
                    "part_number",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("quantity", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Unified",
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
                ("bom_pn", models.CharField(blank=True, max_length=100, null=True)),
                ("bom_qty", models.IntegerField(null=True)),
                ("disti_pn", models.CharField(blank=True, max_length=100, null=True)),
                ("disti_qty", models.IntegerField(blank=True, null=True)),
                ("error_flag", models.CharField(max_length=100)),
            ],
        ),
    ]
