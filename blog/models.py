from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Slider(models.Model):
    authorSlider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titleSlider = models.CharField(max_length=200)
    imagesSlider = models.ImageField(null = True, blank = True, upload_to = "sliders/")


class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')
    

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200, default='tech')
    images = models.ImageField(null = True, blank = True, upload_to = "images/")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title