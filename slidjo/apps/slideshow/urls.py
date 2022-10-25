from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('events/', views.EventList.as_view()),
    path(
            'event/<int:pk>/<str:event_name>',
            views.EventDetail.as_view(),
            name='event-detail'
        ),
    path('events/add/', views.EventCreate.as_view(), name='event-add'),
    path('slideshows/', views.slideshows),
    path('slide/', views.active_slideshow),
    path('slide/<str:show_slug>', views.play_requested_slideshow),
    path('slideshows/add/', views.SlideCreate.as_view(), name='slideshow-add'),
    path('slideshows/add/new', views.slideshow_add_file),
    path('slideshows/add/select', views.slideshow_select_file),
    # path('slideshow/details', views.slideshow_partial),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
