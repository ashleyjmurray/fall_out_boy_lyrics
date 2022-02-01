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

def make_markov_fun():
    f = open('Lyrics_FallOutBoy.json')
    data = json.load(f)

    songs = data['songs']
    lyrics = []
    for x in songs:
        lyrics.append(x['lyrics'])

    lyrics_e = []
    for x in lyrics:
        temp = x.split('Lyrics\n')[1]
        lyrics_e.append(re.sub('\d{1,7}Embed', '', temp).lower())
        
    text = ' '.join(lyrics_e)

    model = markovify.NewlineText(text)
    
    lyrics_temp = []

    for i in range(10):
        model_sentence = model.make_sentence()
        if model_sentence is not None:
            lyrics_temp.append(model_sentence)
            
    return lyrics_temp
