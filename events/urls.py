from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from .views import EventsView, event_detail

urlpatterns = [

    path('',EventsView.as_view( context_object_name = 'events'), name='events'),
    path('<int:id>/', event_detail, name='eventdetail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)