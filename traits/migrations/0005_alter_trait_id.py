# Generated by Django 4.1.3 on 2022-12-01 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("traits", "0004_remove_trait_pets"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trait",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
