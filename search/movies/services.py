from movies.models import Movie


def search_movies_service(title: str, site: str):
    """Search movies based on title and source site"""

    movies = Movie.objects.all()

    if title:
        movies = movies.filter(title__icontains=title)

    if site:
        movies = movies.filter(source_site=site)

    return [
        {
            "title": movie.title,
            "url": movie.url,
            "poster_url": movie.poster_url,
            "source_site": movie.source_site
        }
        for movie in movies
    ]
