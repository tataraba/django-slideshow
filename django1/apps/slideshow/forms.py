from django.forms import ModelForm

from .models import Event, SlideShow


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        labels = {
            'event_name': 'Event Name',
            'event_start_date': 'Event Start Date',
            'event_end_date': 'Event End Date',
            'venue': 'Venue',
            'presentation_date': 'Presentation Date',
            'website': 'Event Website',
            'contact_email': 'Contact Email',
            'slug': 'Slug'
        }


class SlideShowForm(ModelForm):
    class Meta:
        model = SlideShow
        fields = ['title, subject, abstract, content_in_md, slug, length_in_minutes']
        labels = {
            'title': 'Slideshow Title',
            'subject': 'Subject of Slideshow',
            'abstract': 'Abstract',
            'content_in_md': 'Markdown Content',
            'slug': 'Slug',
            'length_in_minutes': 'Length (minutes)'
        }
