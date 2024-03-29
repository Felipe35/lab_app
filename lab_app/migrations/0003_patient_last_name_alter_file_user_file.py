# Generated by Django 4.2.2 on 2023-12-16 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lab_app", "0002_rename_file_file_user_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="last_name",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="file",
            name="user_file",
            field=models.FileField(null=True, upload_to="files"),
        ),
    ]
