from django1.apps.slideshow.models import Event, SlideShow
from django.contrib import admin

# Register your models here.

admin.site.register([SlideShow, Event])
