from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from urllib.parse import quote_plus
from django.db.models import F,Count
from django.http import JsonResponse
from .models import Event, Location

def event_detail(request,id):
    location = get_object_or_404(Location, id=id)
    events = Event.objects.filter(location=location)
    template = "event_detail.html"
    context = {
        'location':location,
        'events':events
    }

    return render(request, template, context)

class EventsView(ListView):
    model = Location
    paginate_by = 2
    context_object_name = 'events'
    template_name = 'events.html'

