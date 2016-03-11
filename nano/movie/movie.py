class Movie():
    def __init__(self, movie_title, movie_story_line, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_story_line
        self.poseter_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #double underscore indicates special functino/method
    #init always takes self as a parameter
    #constructor: the init function that sets up the construction of a class instance
    
