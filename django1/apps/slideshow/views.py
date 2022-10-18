import logging
from pathlib import Path

from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from render_block import render_block_to_string

from .models import Event, SlideShow

logger = logging.getLogger(__name__)


class EventList(ListView):
    template_name: str = 'slideshow/events.html'
    model = Event
    context_object_name = "events"

    def get(self, request, *args, **kwargs):

        if request.headers.get("Event-ID-More"):
            events = Event.objects.all()
            event = events.get(id=request.headers.get("Event-ID-More"))
            html = render_block_to_string(
                "slideshow/partials/event_list.html",
                "more_details",
                {"more_details_visible": True, "show_less_button": True, "event": event},
                request=request
            )
            return HttpResponse(html)

        elif request.headers.get("Event-ID-Less"):
            events = Event.objects.all()
            event = events.get(id=request.headers.get("Event-ID-Less"))
            html = render_block_to_string(
                "slideshow/partials/event_list.html",
                "more_details",
                {"more_details_visible": False, "show_less_button": False, "event": event},
                request=request
            )
            return HttpResponse(html)
        events = Event.objects.all()
        return render(request, self.template_name, {"events": events})


class EventDetail(DetailView):
    template_name: str = 'slideshow/event.html'
    model = Event
    context_object_name = "event"


class EventCreate(CreateView):
    template_name: str = 'slideshow/event_create.html'
    model = Event
    context_object_name = "event"
    fields = [
        "slideshow",
        "name",
        "venue",
        "city",
        "state",
        "country",
        "start_date",
        "end_date",
        "presentation_date",
        "website",
        "presentation_video",
        "contact_email"
    ]
    success_url = "/events"

    def get(self, request, *args, **kwargs):
        shows = SlideShow.objects.all()
        form = self.get_form()
        context = {
            "shows": shows,
            "form": form
        }
        return render(request, self.template_name, context)


class SlideCreate(CreateView):
    template_name = 'slideshow/slideshow_create.html'
    model = SlideShow
    context_object_name = "slideshow"
    fields = [
        "author",
        "title",
        "abstract",
        "slide_file",
        "featured",
        "length_in_minutes"
    ]
    success_url = "/slideshows"

    def get(self, request, *args, **kwargs):
        files = Path(settings.MEDIA_ROOT / "slides").glob('*.htm*')
        form = self.get_form()
        context = {
            "files": files,
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if not request.POST.get("slideshow"):
            return self.form_valid(form)
        else:
            print(form.instance)
            slideshow_path = Path(
                settings.MEDIA_ROOT / "slides" / request.POST.get("slideshow"))
            print(f'{slideshow_path=}')
            # print(form.instance.featured)
            form.instance.slide_file = slideshow_path
            print(form.instance.slide_file)
            return redirect("/slideshows")
            # return self.form_valid(form)
            # return self.form_invalid(form)


# Create your views here.
def index(request):
    shows = SlideShow.objects.all()
    if request.headers.get("HX-Request"):
        print("Index hx header")
        html = render_block_to_string(
            "slideshow/index.html",
            "set_show",
            {"setting_block": True, "shows": shows},
            request=request
        )
        return HttpResponse(html)
    if request.POST:
        featured_show = shows.filter(featured__exact=True)
        if featured_show:
            for show in featured_show:
                print(show.slide_file)
                show.featured = False
                show.save()
        show_id = request.POST.get("slideshow")
        show = shows.get(id=show_id)
        show.featured = True
        show.save()
        render(
            request,
            "slideshow/index.html",
            {
                "shows": shows,
            }
        )
    return render(
        request,
        "slideshow/index.html",
        {
            "shows": shows,
        }
    )


def slideshows(request: HttpRequest):

    if request.headers.get("Show-ID"):
        shows = SlideShow.objects.all()
        show = shows.get(id=request.headers.get("Show-ID"))
        abstract_list = [line for line in show.abstract.splitlines() if line]
        print(abstract_list)
        html = render_block_to_string(
            "slideshow/partials/slideshow_list.html",
            "show_abstract",
            context={"show": show, "abstract_list": abstract_list},
            request=request
        )
        return HttpResponse(html)

    shows = SlideShow.objects.all()

    return render(request, 'slideshow/slideshows.html', {'shows': shows})


def slideshow_add_file(request: HttpRequest):
    # Only works when user logged in. Need to add logic for anonymous user.
    author_id = request.user.id
    author = User.objects.get(id=author_id)
    if request.headers.get("HX-Request"):
        html = render_block_to_string(
            "slideshow/forms/slideshow_form.html",
            "add_or_select_slide",
            context={"add": True, "slide_author": author},
            request=request
        )

        return HttpResponse(html)
    return render(request, 'slideshow/slideshows.html')


def slideshow_select_file(request: HttpRequest):
    # Only works when user logged in. Need to add logic for anonymous user.
    author_id = request.user.id
    author = User.objects.get(id=author_id)
    files = Path(settings.MEDIA_ROOT / "slides").glob('*.htm*')
    if request.headers.get("HX-Request"):
        html = render_block_to_string(
            "slideshow/forms/slideshow_form.html",
            "add_or_select_slide",
            context={"select": True, "files": files, "slide_author": author},
            request=request
        )

        return HttpResponse(html)
    return render(request, 'slideshow/slideshows.html')


@xframe_options_exempt
def active_slideshow(request):
    shows = SlideShow.objects.all()
    print(request)
    if request.method == "POST":
        print("post method")
        return render(request, "slideshow/slide.html")
    try:
        featured_show = shows.get(featured=True)
        slide_file = Path(settings.MEDIA_ROOT / str(featured_show.slide_file))
        slide_text = slide_file.read_text()
        return render(request, "slideshow/slide.html", {"slide_text": slide_text})
    except ObjectDoesNotExist:
        print("what the hell")
        return render(request, "slideshow/index.html")


@xframe_options_exempt
def play_requested_slideshow(request, show_slug):
    shows = SlideShow.objects.all()
    selected_show = shows.get(slug=show_slug)
    slide_file = Path(settings.MEDIA_ROOT / str(selected_show.slide_file))
    slide_text = slide_file.read_text()
    return render(request, "slideshow/slide.html", {"slide_text": slide_text})
