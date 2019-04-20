from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Contact(models.Model):
    email = models.EmailField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.email

class Post(models.Model):
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=200)
    description = models.TextField()
    published = models.DateTimeField(default=timezone.now())
    image = models.FileField(null=True, blank=True)
    views = models.CharField(blank=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug}) 
         

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    comment = models.TextField()
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.comment
    

