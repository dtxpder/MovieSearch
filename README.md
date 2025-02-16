# Film & TV Extractor

This is a Django and React-based application that allows users to search for movies and TV shows by title and source site. The project uses Docker Compose for easy deployment.

## Features

- Search for movies and TV shows by title
- Filter results by site, such as fmovies24.to and gogoflix.stream
- Display movie details including title, poster, and source link
- Django REST API for the backend
- React with Vite for the frontend

## Tech Stack

- **Frontend**: React.js
- **Backend**: Django
- **Database**: SQLite

## Installation and Setup
### Step 1: Clone the repository
```sh
git clone URL
```

### Step 2: Navigate to the project directory
```sh
cd search
```
### Step 3: Start the application using Docker Compose
```sh
docker-compose up --build
```
Then access the service at http://localhost:5173

## API Endpoints
**GET** /api/movies/?title=&lt;title&gt;&site=&lt;site&gt;

Query Parameters:
- title: Required. Movie title, for example, "Top"
- site: Optional. Filter by site, such as fmovies24.to, gogoflix.stream, or all
```json
[
  {
    "title": "The Matrix",
    "url": "https://fmovies24.to/movie/the-matrix-jy58",
    "poster_url": "https://image.tmdb.org/t/p/w500/matrix.jpg",
    "source_site": "fmovies24.to"
  }
]
```
