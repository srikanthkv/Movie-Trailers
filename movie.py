# Class Movie contains 4 instance variables:
# Title, Storyline, Poster and Trailer


class Movie():
    def __init__(self, title, storyline, trailer_youtube, poster_image):
        # Initialize the parameters
        self.title = title
        self.storyline = storyline
        self.trailer_youtube_url = trailer_youtube
        self.poster_image_url = poster_image
