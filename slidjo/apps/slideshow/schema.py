from djantic import ModelSchema
from slidjo.apps.slideshow.models import Event, SlideShow


class SlideShowSchema(ModelSchema):
    class Config:
        model = SlideShow


class EventSchema(ModelSchema):
    class Config:
        model = Event
