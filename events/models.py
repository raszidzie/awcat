from django.db import models



class Location(models.Model):
   
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.country

class Event(models.Model):
    event_name = models.CharField(max_length=150)
    event_description = models.TextField()
    event_location = models.CharField(max_length=200)
    event_datetime = models.DateTimeField()
    image = models.FileField(null=True, blank=True)
    views = models.CharField(blank=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    location = models.ForeignKey(Location, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name