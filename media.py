import urllib2
import json


class Movie:
    def __init__(self, title, poster, trailer):
        self.title = title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer


def load_data(url):
    data = json.load(urllib2.urlopen(url))

    # 'Title'
    #if
    #
    return data