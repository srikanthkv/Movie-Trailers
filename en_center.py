import movie
import fresh_tomatoes

# Objects of the Class Movie for 6 different movies. Each Object contains
# Title, Short Description, Youtube Trailer URL and Poster Image URL.

lights_out = movie.Movie(
    "Lights out",
    "Lights Out is a 2016 American supernatural horror film directed by " +
    "David F.cSandberg in his major directorial debut,produced by Lawrence" +
    "Grey, James Wan and Eric Heisserer and written by Heisserer.",
    "https://www.youtube.com/watch?v=6LiKKFZyhRU",
    "https://upload.wikimedia.org/wikipedia/en/d/dc/Lights_Out_2016_poster.jpg")  # NOQA

It = movie.Movie(
    "IT",
    "It is a 2017 American supernatural horror film based on Stephen " +
    "King's 1986 novel of the same name.",
    "https://www.youtube.com/watch?v=xKJmEC5ieOk",
    "https://upload.wikimedia.org/wikipedia/en/a/a2/It_%282017%29_logo.jpg")

annabelle = movie.Movie(
    "Annabelle",
    "Annabelle is a 2014 American supernatural horror film directed by John " +
    "R.Leonetti, written by Gary Dauberman and produced by Peter Safran and " +
    "James Wan",
    "https://www.youtube.com/watch?v=11taaQy2KBg",
    "https://upload.wikimedia.org/wikipedia/en/9/9b/Annabelle-poster.jpg")

conjuring = movie.Movie(
    "The Conjuring",
    "The Conjuring is a 2013 American supernatural horror film directed by " +
    "James Wan and written by Chad Hayes and Carey W. Hayes",
    "https://www.youtube.com/watch?v=VFsmuRPClr4",
    "https://upload.wikimedia.org/wikipedia/en/1/1f/Conjuring_poster.jpg")

hush = movie.Movie(
    "Hush",
    "Hush is a 2016 American horror thriller film directed and edited by " +
    "Mike Flanagan, starring Kate Siegel, and written by both.",
    "https://www.youtube.com/watch?v=Q_P8WCbhC6s",
    "https://upload.wikimedia.org/wikipedia/en/e/e3/Hush_2016_poster.jpg")

onefour = movie.Movie(
    "1408",
    "1408 is a 2007 American psychological horror film based on Stephen" +
    " King's 1999 short story of the same name.",
    "https://www.youtube.com/watch?v=WIASqPZqnhs",
    "https://upload.wikimedia.org/wikipedia/en/6/63/1408poster.jpg")

# Array/List to hold all the Movie objects
movie_list = [lights_out, It, annabelle, conjuring, hush, onefour]

# Calling method from fresh_tomatoes.py (Imported) which
# creates a HTML page and opens it.
fresh_tomatoes.open_movies_page(movie_list)
