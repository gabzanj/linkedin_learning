import pandas as pd


classic_rock_songs = {
    "Song Name": ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California", "Imagine",
                  "Smells Like Teen Spirit", "Another One Bites the Dust"],
    "Artist": ["Queen", "Led Zeppelin", "Eagles", "John Lennon", "Nirvana", "Queen"],
    "Release Year": [1975, 1971, 1976, 1971, 1991, 1980],
    "Album": ["A Night at the Opera", "IV", "Hotel California", "Imagine", "Nevermind", "The Game"],
    "Duration (minutes)": [6.05, 8.02, 6.30, 3.03, 5.01, 3.36]
}

df_classic_rock_songs = pd.DataFrame(classic_rock_songs)

df_release_year_greater_than_1975 = df_classic_rock_songs.query("`Release Year` > 1975")

max_duration = 5.30
df_duration_less_than_max = df_classic_rock_songs.query("`Duration (minutes)` < @max_duration")

artist = "Queen"
min_year = 1978
df_artist_and_after_min_year = df_classic_rock_songs.query("Artist == @artist & `Release Year` > @min_year")
