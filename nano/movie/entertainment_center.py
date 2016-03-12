import movie
#tells program to use contents of movie.py

toy_story = movie.Movie('Toy Story',
                        'A story of a boy and his toys',
                        'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = movie.Movie("avatar", "pocahontas ripoff", "poster image link", "youtu link")

#instance variables: the parameters within an instance of a class

print(toy_story.trailer_youtube_url)
toy_story.show_trailer()
