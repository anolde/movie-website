import media
import fresh_tomatoes


stepmom = media.Movie("Stepmom",
                      "A story of a mother who is replaced by a new wife.", "https://1cqgxm3l59yi2wwbnn3qy35h-wpengine.netdna-ssl.com/wp-content/uploads/2008/12/dvd-cover3.jpg",  # noqa
                      "1998",
                      "https://www.youtube.com/watch?v=T8sAXDUFSCs",
                      "5.1/10")
print(stepmom.storyline)

white_chicks = media.Movie("White Chicks",
                            "Two FBI agents must disguise themselves completely.",  # noqa
                            "https://images-na.ssl-images-amazon.com/images/I/516pTmL6guL.jpg",  # noqa
                            "2004",
                            "https://www.youtube.com/watch?v=aeVkbNka9HM",  # noqa
                            "3.7/10")
print(white_chicks.storyline)

labyrinth = media.Movie("Labyrinth",
                        "A young girl negotiates with a goblin king",
                        "https://www.landmarktheatres.com/image?url=http://landmark.filmdb.peachcinemas.com/FilmImages/21/1/2634/Labyrinth_224x332.png",  # noqa
                        "1986",
                        "https://www.youtube.com/watch?v=WT_xpFZe20A",
                        "6.3/10")
print(labyrinth.storyline)

harry_potter = media.Movie("Harry Potter",
                           "Fifth year wizard Harry Potter faces character defamation when he claims that He Who Must Not Be Named has                 returned.",  # noqa
                           "https://images-na.ssl-images-amazon.com/images/I/51acekLm3uL._SY445_.jpg",  # noqa
                           "2007",
                           "https://www.youtube.com/watch?v=WS8Jbm8Gob4",
                           "6.9/10")

greys_anatomy = media.TvShow("Greys Anatomy",
                             "A doctor has to juggle her professional goals with her romantic interests as a budding surgeon.",  # noqa
                             "https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Grey%27s_Anatomy_season_12_dvd.jpg/240px-Grey%27s_Anatomy_season_12_dvd.jpg",  # noqa
                             "2005",
                             "14",
                             "ABC",
                             "Losing My Religion",
                             "https: // www.youtube.com/watch?v=icXooBKhelc")

buffy = media.TvShow("Buffy",
                     "One girl is chosen to defend the world against vampires, and the forces of darkness.",  # noqa
                     "https://images-na.ssl-images-amazon.com/images/I/51DJ570H6VL._SX342_.jpg",  # noqa
                     "1997",
                     "7",
                     "FOX",
                     "Welcome To the HellMouth",
                     "https://www.youtube.com/watch?v=-1v_q6TWAL4")
favorites = [stepmom, white_chicks, labyrinth,
             harry_potter, buffy, greys_anatomy]


# use fresh tomatoes built by udacity
fresh_tomatoes.open_movies_page(favorites)

# white_chicks.show_trailer()

print(media.Movie.__doc__)
