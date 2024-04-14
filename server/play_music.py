import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide' # Suppress Pygame welcome message

import pygame as pg

def play_song(song_path):
    pg.init()
    pg.mixer.init()
    pg.mixer.music.load(song_path)
    pg.mixer.music.play()

def stop_song():
    pg.mixer.music.stop()