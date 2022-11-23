from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PaintStyle",
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
                ("model_name", models.CharField(blank=True, max_length=70)),
                ("model_urls", models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Painting",
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
                ("title", models.CharField(blank=True, max_length=70)),
                ("content", models.CharField(blank=True, max_length=250)),
                ("before_image", models.ImageField(blank=True, upload_to="before_img")),
                ("after_image", models.ImageField(blank=True, upload_to="after_img")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "paint_style",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="paintings.paintstyle",
                    ),
                ),
            ],
            options={
                "db_table": "db_painting",

            },
        ),
    ]
