# Generated by Django 4.2.2 on 2023-12-16 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lab_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="file",
            old_name="file",
            new_name="user_file",
        ),
    ]