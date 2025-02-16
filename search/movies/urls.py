from django.urls import path
from .views import search_movies

urlpatterns = [
    path("api/movies/", search_movies, name="search-movies"),
]
