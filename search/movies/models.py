from django.db import models

class Movie(models.Model):
    TYPE_CHOICES = [
        ('movie', 'Movie'),
        ('tv_show', 'TV Show')
    ]

    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    release_year = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    poster_url = models.URLField(null=True, blank=True)
    source_site = models.CharField(max_length=100)  # fmovies24.to / gogoflix.stream
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)  # movie / tv_show

    def __str__(self):
        return self.title
