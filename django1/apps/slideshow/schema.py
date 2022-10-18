from django1.apps.slideshow.models import Event, SlideShow
from djantic import ModelSchema


class SlideShowSchema(ModelSchema):
    class Config:
        model = SlideShow


class EventSchema(ModelSchema):
    class Config:
        model = Event

