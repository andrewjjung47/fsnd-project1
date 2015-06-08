import urllib2
import json

from api_key import YOUTUBE_API_KEY


def load_data(url):
    # Load json returned from a url
    try:
        data = json.load(urllib2.urlopen(url))
        return data
    except urllib2.HTTPError:
        return None


def get_movie(title, year):
    """Constructs a Movie object using title and year.
    OMDB API is used to fetch official title and poster image url."""
    omdb_url = 'http://www.omdbapi.com/?t=%s&y=%s&plot=short&r=json' \
        % (title, year)
    omdb_url_no_space = omdb_url.replace(' ', '+')
    movie_data = load_data(omdb_url_no_space)

    if movie_data is not None:
        if movie_data['Response'] == 'True':
            title = movie_data['Title']
            poster_image_url = movie_data['Poster']
            return Movie(title, year, poster_image_url)
        else:
            print movie_data['Error']
            return None


class Movie:
    def search_trailers(self):
        # Search youtube trailer using self.title
        query = ('movie+%s+%s+trailer' %
                 (self.title, self.year)).replace(' ', '+')
        # Get the closest matching video url
        search_url = 'https://www.googleapis.com/youtube/v3/search\
?order=relevance&part=snippet&q=%s=EN\
&type=video&regionCode=US&maxResults=1&key=%s' % (query, YOUTUBE_API_KEY)
        trailer_data = load_data(search_url)
        if (trailer_data['kind'] == 'youtube#searchListResponse'):
            trailer_id = trailer_data['items'][0]['id']['videoId']

            video_url = 'https://www.youtube.com/watch?v=%s' % trailer_id
            print video_url
            return video_url

    def __init__(self, title, year, poster, trailer=None):
        self.title = title
        self.year = year
        self.poster_image_url = poster
        self.trailer_youtube_url = self.search_trailers()

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title
