import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import lyricsgenius as lg

songs = pd.read_csv("songs.csv", sep=";")
songs.head()

def search_lyrics(song_title, artist_name):
    access_token = '8yvpmDv96aodI5vg660Afcby4XPdrhPrx4JCAM3souNcRYG9C2nF5TWg1'
    genius = lg.Genius(access_token)
    song = genius.search_song(song_title, artist_name)
    return song.lyrics if song is not None else None

song_lyrics = pd.DataFrame(columns=['lyrics'], index=songs.index)

song_lyrics = pd.read_csv('song_lyrics.csv', sep=';')
for index, row in songs.iterrows():
    if pd.isnull(song_lyrics.loc[index]['lyrics']):
        try:
            song_lyrics.loc[index] = search_lyrics(row['title'], row['artist'])
            song_lyrics.to_csv('song_lyrics.csv', sep=';')
        except:
            continue