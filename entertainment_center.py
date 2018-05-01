import fresh_tomatoes
import media

# Here are 6 movie objects, each one has three attrs:
# Title of the movie, Box art imagery, link to the movie trailer.
# The number of movie objects can be arbitrary.
thor = media.Movie("Thor: Ragnarok",
                   "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=v7MGUNV8MxU")
ready_player_one = media.Movie("Ready Player One",
                               "https://upload.wikimedia.org/wikipedia/en/7/74/Ready_Player_One_%28film%29.png",  # NOQA
                               "https://www.youtube.com/watch?v=cSp1dM2Vj48")
avengers = media.Movie("Avengers 3: Infinity War",
                       "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=m2uqb2bt_bs")
mission_impossible = media.Movie("Mission: Impossible - Rogue Nation",
                                 "https://upload.wikimedia.org/wikipedia/en/f/fb/Mission_Impossible_Rogue_Nation_poster.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=gOW_azQbOjw")
sao = media.Movie("Sword Art Online - Ordinal Scale",
                  "https://upload.wikimedia.org/wikipedia/en/b/ba/Sword_Art_Online_The_Movie_-_Ordinal_Scale_Visual.jpg",  # NOQA
                  "https://www.youtube.com/watch?v=AoczqQXG74A")
pokemon = media.Movie("Pokemon the Movie: Everyone's Story",
                      "https://upload.wikimedia.org/wikipedia/en/e/e7/PokeMovie21.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=9hFXh25UwLU")

# Put all objects into an array.
# If the number of objects has been modified, remember to modify this, too.
movies = [thor, ready_player_one, avengers, mission_impossible, sao, pokemon]

fresh_tomatoes.open_movies_page(movies)  # Generate a html file and open it
