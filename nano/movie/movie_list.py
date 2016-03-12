import movie
import fresh_tomatoes

harry_potter_one = movie.Movie("Harry Potter and the Sorcerer's Stone",
                               "A sttory of a young boy who discovers a magical secret",
                               "https://upload.wikimedia.org/wikipedia/en/6/6b/Harry_Potter_and_the_Philosopher%27s_Stone_Book_Cover.jpg",
                               "https://www.youtube.com/watch?v=VyHV0BRtdxo")

toy_story = movie.Movie('Toy Story',
                        'A story of a boy and his toys',
                        'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

fellowship = movie.Movie("Lord of the Rings: The Fellowship of the Ring",
                         "An epic tale of most unlikely proportions",
                         "https://upload.wikimedia.org/wikipedia/en/8/87/Ringstrilogyposter.jpg",
                         "https://www.youtube.com/watch?v=V75dMMIW2B4")

guardians_of_the_galaxy = movie.Movie("The Guardians of the Galaxy",
                        "A tale of the radest, baddest, actually worst heroes ever",
                        "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                        "https://www.youtube.com/watch?v=B16Bo47KS2g")

empire_strikes_back = movie.Movie("Star Wars Episode V: the Empire Strikes Back",
                                  "The saga continues as luke plans to face his darkest fears",
                                  "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                                  "https://www.youtube.com/watch?v=JNwNXF9Y6kY")

crazy_stupid_love = movie.Movie("Crazy, Stupid, Love",
                                "A tale of love, loss, and rekindling",
                                "https://upload.wikimedia.org/wikipedia/en/7/78/CrazyStupidLovePoster.jpg",
                                "https://www.youtube.com/watch?v=aDLhjm-0rJQ")

movies = [harry_potter_one, toy_story, fellowship, guardians_of_the_galaxy, empire_strikes_back, crazy_stupid_love]

fresh_tomatoes.open_movies_page(movies)
