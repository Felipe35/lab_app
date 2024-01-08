# Generated by Django 4.2.2 on 2023-12-16 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lab_app", "0006_alter_patient_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="file",
            name="slug",
        ),
        migrations.AddField(
            model_name="patient",
            name="slug",
            field=models.SlugField(blank=True, default=""),
        ),
    ]
