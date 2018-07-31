import media
import fresh_tomatoes

stepmom = media.Movie("Stepmom", "A story of a mother who is replaced by a new wife and has cancer", "https://1cqgxm3l59yi2wwbnn3qy35h-wpengine.netdna-ssl.com/wp-content/uploads/2008/12/dvd-cover3.jpg", "1998", "https://www.youtube.com/watch?v=T8sAXDUFSCs", "5.1/10")
print(stepmom.storyline)

white_chicks = media.Movie("White Chicks", "A story of two FBI agents who must solve a crime by posing as two famous white socialite sisters.", "https://images-na.ssl-images-amazon.com/images/I/516pTmL6guL.jpg", "2004", "https://www.youtube.com/watch?v=aeVkbNka9HM", "3.7/10")
print(white_chicks.storyline)

labyrinth = media.Movie("Labyrinth", "A young girl regrets her wish for a goblin king to take her little brother away", "https://www.landmarktheatres.com/image?url=http://landmark.filmdb.peachcinemas.com/FilmImages/21/1/2634/Labyrinth_224x332.png", "1986", "https://www.youtube.com/watch?v=WT_xpFZe20A", "6.3/10")
print(labyrinth.storyline)

harry_potter = media.Movie("Harry Potter & the Order of the Phoenix", "Fifth year wizard Harry Potter faces character defamation when he claims that He Who Must Not Be Named has returned.", "https://images-na.ssl-images-amazon.com/images/I/51acekLm3uL._SY445_.jpg", "2007", "https://www.youtube.com/watch?v=WS8Jbm8Gob4", "6.9/10")

buffy = media.TvShow("Buffy the Vampire Slayer", "One girl is chosen to defend the world against vampires, and the forces of darkness.", "https://images-na.ssl-images-amazon.com/images/I/51DJ570H6VL._SX342_.jpg", "1997", "7", "FOX", "Welcome To the HellMouth", "https://www.youtube.com/watch?v=-1v_q6TWAL4") 
favorites = [stepmom, white_chicks, labyrinth, harry_potter, buffy]

## use fresh tomatoes built by udacity ##
fresh_tomatoes.open_movies_page(favorites)

#white_chicks.show_trailer()

print(media.Movie.__doc__)
print(harry_potter.__name__)
