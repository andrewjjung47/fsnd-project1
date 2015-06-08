import media
import fresh_tomatoes


def get_favorite_movies(movie_list):
    movies = []
    for movie in movie_list:
        title = movie['title']
        year = movie['year']
        movie_object = media.get_movie(title, year)
        if (movie_object is not None):
            movies.append(movie_object)
    return movies

favorite_movie_list = [
    {
        'title': 'Frozen',
        'year': 2013
    },
    {
        'title': 'The Matrix',
        'year': 1999
    },
    {
        'title': 'A Beautiful Mind',
        'year': 2001
    },
    {
        'title': 'Cast Away',
        'year': 2000
    },
    {
        'title': 'Dead Poets Society',
        'year': 1989
    },
    {
        'title': 'Star Wars',
        'year': 2005
    }
]

favorite_movies = get_favorite_movies(favorite_movie_list)
print favorite_movies


fresh_tomatoes.open_movies_page(favorite_movies)