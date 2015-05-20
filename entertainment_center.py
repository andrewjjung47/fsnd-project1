import media
import fresh_tomatoes

data = media.load_data('http://www.omdbapi.com/?t=Frozen&y=&plot=short&r=json')
frozen = media.Movie(data['Title'], data['Poster'], 'https://www.youtube.com/watch?v=L0MK7qz13bU')

fresh_tomatoes.open_movies_page([frozen])