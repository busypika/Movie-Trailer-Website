import fresh_tomatoes
import media

thor = media.Movie("Thor: Ragnarok",
                   "Thunderlords!",
                   "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
                   "https://www.youtube.com/watch?v=v7MGUNV8MxU")
ready_player_one = media.Movie("Ready Player One",
                        "A war on Oasis",
                        "https://upload.wikimedia.org/wikipedia/en/7/74/Ready_Player_One_%28film%29.png",
                        "https://www.youtube.com/watch?v=cSp1dM2Vj48")
avengers = media.Movie("Avengers 3: Infinity War",
                      "Here comes the Thanos",
                      "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                      "https://www.youtube.com/watch?v=m2uqb2bt_bs")
mission_impossible = media.Movie("Mission: Impossible - Rogue Nation",
                                 "Ethan Hunt is back!",
                                 "https://upload.wikimedia.org/wikipedia/en/f/fb/Mission_Impossible_Rogue_Nation_poster.jpg",
                                 "https://www.youtube.com/watch?v=gOW_azQbOjw")
sao = media.Movie("Sword Art Online - Ordinal Scale",
                  "Kirito, the Black Swordsman",
                  "https://upload.wikimedia.org/wikipedia/en/b/ba/Sword_Art_Online_The_Movie_-_Ordinal_Scale_Visual.jpg",
                  "https://www.youtube.com/watch?v=AoczqQXG74A")
pokemon = media.Movie("Pokemon the Movie: Everyone's Story",
                     "Pikachu!",
                     "https://upload.wikimedia.org/wikipedia/en/e/e7/PokeMovie21.jpg",
                     "https://www.youtube.com/watch?v=9hFXh25UwLU")
movies = [thor, ready_player_one, avengers, mission_impossible, sao, pokemon]
fresh_tomatoes.open_movies_page(movies)

