# Generated by Django 4.2.2 on 2023-12-16 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lab_app", "0004_alter_file_options_file_slug"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="file",
            options={"verbose_name_plural": "File Entries"},
        ),
    ]
