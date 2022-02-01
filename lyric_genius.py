import re
import markovify
import warnings
from bs4 import BeautifulSoup
import pandas as pd
import requests
import lyricsgenius as lg
import json
import numpy
import itertools

def get_fall_out_boy():
    genius_token = 'insert token here'

    url = 'https://en.wikipedia.org/wiki/List_of_songs_recorded_by_Fall_Out_Boy'
    page = requests.get(url)
    html = page.content

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', attrs={'class':'wikitable sortable plainrowheaders'})
    table_body = table.find('tbody')
    rows = table_body.find_all('th', {'scope':'row'})

    fob_songs = []
    for x in rows:
        text = x.text
        fob_songs.append(text.replace('"', '').replace(' \n', '').replace('\n', ''))
        
    genius = lg.Genius(genius_token,
    skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
    artist = genius.search_artist("Fall Out Boy", max_songs=0, sort="title", include_features=False)

    def lyric_adder(title):
        song = genius.search_song(title, 'Fall Out Boy')
        artist.add_song(song)
        
    fob_songs.remove('Stayin Out All Night (Boys of Zummer Remix)')

    for fob in fob_songs:
        lyric_adder(fob)
        
    artist.save_lyrics()
