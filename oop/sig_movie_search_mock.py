from __future__ import annotations

from movie import Movie
import csv


class MovieSearch:
    """Loads a movie database and supports year-range and genre queries."""

    def __init__(self, csv_path: str) -> None:
        # TODO: Read csv_path and store the movies for later searches.
        # You may add helper methods and instance attributes.
        with open(csv_path, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)

            required = {'id', 'title', 'year', 'genres'}
            if reader.fieldnames is None or not required.issubset(reader.fieldnames):
                raise ValueError('Missing required fields in CSV file.')
            
            self.movies = []
            seen = set()
            for row in reader:
                if any(row.get(column) is None for column in required):
                    raise ValueError('Missing or empty columns in CSV file.')
                id = int(row['id'])
                title = row['title'].strip()
                if not title:
                    raise ValueError('Empty title in CSV file.')
                year = int(row['year'])
                genres = tuple(
                    genre.strip()
                    for genre in row['genres'].split('|')
                    if genre.strip()
                )
                if not genres:
                    raise ValueError('No usable genres in CSV row.')

                if id in seen:
                    continue
                seen.add(id)

                movie = Movie(id, title, year, genres)                

                self.movies.append(movie)

    def search(self, start_year: int, end_year: int, genre: str) -> list[Movie]:
        """Return unique matching movies sorted by year, then title.

        Rules:
        - The year range is inclusive.
        - Genre matching is case-insensitive and ignores surrounding spaces.
        - A movie can contain several pipe-separated genres.
        - Return each movie ID at most once.
        """
        # TODO: Implement this method.
        if start_year > end_year:
            raise ValueError('Invalid year range')
        genre = genre.strip().casefold()
        if not genre:
            raise ValueError('Invalid genre')
        matching_movies = []
        for movie in self.movies:
            if start_year <= movie.year <= end_year and any(genre == movie_genre.casefold() for movie_genre in movie.genres):
                matching_movies.append(movie)
        
        matching_movies.sort(key=lambda movie:(movie.year, movie.title.casefold()))

        return matching_movies
