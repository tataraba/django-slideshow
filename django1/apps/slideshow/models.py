import logging
from pathlib import Path

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

logger = logging.getLogger(__name__)


def slides_path():
    return Path(settings.BASE_DIR / "django1/apps/slideshow/templates/slideshow/slides")


class SlideShow(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=512, unique=True)
    abstract = models.TextField(blank=True)
    slide_file = models.FileField(
        upload_to=str("slides"), null=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True)
    length_in_minutes = models.IntegerField()

    class Meta:
        verbose_name = "slideshow"
        verbose_name_plural = "slideshows"

    def __str__(self):
        return f'{self.author}: {self.title}'

    def get_absolute_url(self):
        return reverse("slideshow_detail", args=[str(self.pk)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        # select any featured item
        qs = type(self).objects.filter(featured=True)
        if self.id:
            qs = qs.exclude(id=self.id)
        qs.update(featured=False)
        super(SlideShow, self).save(*args, **kwargs)


class Event(models.Model):
    slideshow = models.ForeignKey(SlideShow, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    venue = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=80, blank=True)
    country = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField()
    presentation_date = models.DateField()
    website = models.URLField(blank=True)
    presentation_video = models.URLField(blank=True)
    contact_email = models.EmailField(blank=True)
    slug = models.SlugField(default="", blank=True)

    class Meta:
        verbose_name = "event"
        verbose_name_plural = "events"

    def __str__(self):
        return f'{self.name}: {self.start_date}'

    def get_absolute_url(self):
        return reverse("event-detail", args=[str(self.pk)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)
