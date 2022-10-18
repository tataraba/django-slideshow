# Generated by Django 4.1.1 on 2022-10-05 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("slideshow", "0005_slideshow_slide_file_upload_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="slideshow",
            name="slide_file_upload",
        ),
        migrations.AddField(
            model_name="slideshow",
            name="featured",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="slideshow",
            name="slide_file",
            field=models.FileField(null=True, upload_to="slides"),
        ),
    ]