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
Then access the service at:
- Backend: http://localhost:8000
- Frontend: http://localhost:5173

## API Endpoints
**GET** /api/movies/?title=&lt;title&gt;&site=&lt;site&gt;

Query Parameters:
- title: Required. Movie title, for example, "Top"
- site: Optional. Filter by site, such as fmovies24.to, gogoflix.stream, or all

`Get api/movies/?title=december&site=gogoflix.shop`
```json
[
    {
        "title": "May December",
        "url": "https://gogoflix.shop/categorie-films/26659-may-december-b9h38.html",
        "poster_url": "https://gogoflix.shop/uploads/posts/may-december-XPoa1.webp",
        "source_site": "gogoflix.shop"
    }
]
```
