from django.shortcuts import render
from django.views import generic
from .models import Event


# Create your views here.

class AllAvaliableEvents(generic.ListView):
    model = Event
    template_name = 'list.html'
    context_object_name = 'events'
    queryset = Event.objects.filter(release_events__release_status='released')

    def get_queryset(self):
        return self.queryset
