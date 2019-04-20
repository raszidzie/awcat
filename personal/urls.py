
from django.urls import path
from personal.views import home_view, blog, post_detail, mp3
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', blog, name='blog' ),
    path('audio/<int:id>/', mp3, name='mp3'),
    path('<slug:slug>/', post_detail, name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
