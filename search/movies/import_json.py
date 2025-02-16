import json
from movies.models import Movie

def import_movies_from_json(file_path, source_site):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        print(f"Skipping {file_path}, expected a list at the root level.")
        return

    for task in data:
        result = task.get("result")
        if not isinstance(result, dict):
            print(f"Skipping task {task.get('id')}, 'result' is not a valid dictionary.")
            continue

        movies = result.get("items", [])
        if not isinstance(movies, list):
            print(f"Skipping task {task.get('id')}, 'items' is not a valid list.")
            continue

        for item in movies:
            extracted = item.get("extracted_item")
            if not extracted:
                continue

            url = item.get("source", {}).get("url", "")
            title = extracted.get("label", "Unknown Title")
            release_year = extracted.get("release_year")
            duration = extracted.get("duration_in_minutes")
            poster_url = None

            if extracted.get("posters"):
                poster_data = extracted["posters"][0]
                poster_url = poster_data.get("source", {}).get("url")

            content_type = extracted.get("type")
            if not content_type:
                continue

            Movie.objects.update_or_create(
                url=url,
                defaults={
                    "title": title,
                    "release_year": release_year,
                    "duration": duration,
                    "poster_url": poster_url,
                    "source_site": source_site,
                    "type": content_type
                }
            )

    print(f"Import finished from {source_site}")
