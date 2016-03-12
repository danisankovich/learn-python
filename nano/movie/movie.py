import webbrowser

class Movie():
    def __init__(self, movie_title, movie_story_line, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    #double underscore indicates special functino/method
    #init always takes self as a parameter
    #constructor: the init function that sets up the construction of a class instance
    
#if you remove the self. from one of the instance variables, it can still be accessed within
#the init, but it can't be accessed later because that instance will not have that attribute
