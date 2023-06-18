import pandas as pd
import lyricsgenius as lg
import csv

access_token = '8yvpmDv96aodI5vg660Afcby4XPdrhPrx4JCAM3souNcRYG9C2nF5TWg1'
genius = lg.Genius(access_token)

def get_lyrics(song_title, artist_name):
    song = genius.search_song(song_title, artist_name)
    return song.lyrics if song is not None else ""

songs = pd.read_csv("songs.csv", sep=";")

with open("songs_lyrics.csv", "a", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file, delimiter="|")
    for _, song in songs.iloc[1397:].iterrows():
        is_ok = False
        while not is_ok:
            try:
                lyrics = get_lyrics(song.title, song.artist)
                is_ok = True
                writer.writerow([song.title, song.artist, lyrics])
            except Exception as e:
                continue