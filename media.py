import webbrowser


class Movie():
    """ This class provides a way to store movie related informations.

    This class stores movie related informations like the title of the movie,
    the box art imagery and the link to the movie trailer.
    It also has a 'method show_trailer()' which opens the site of the trailer.

    Attributes:
        title (str): Title of the movie.
        poster_image_url (str): A link to the box art imagery.
        trailer_youtube_url (str):  A link to the movie trailer.

    """

    def __init__(self, movie_tite, poster_image, trailer_youtube):
        self.title = movie_tite
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
