# Generated by Django 4.1.1 on 2022-10-16 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("slideshow", "0013_event_city_event_country_event_state"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="presentation_video",
            field=models.URLField(blank=True),
        ),
    ]
