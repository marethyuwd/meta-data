import os
from mp3_tagger import MP3File as mp3

def tagSong(songtitle,album,artist):
    song= mp3(songtitle)
    song.album = album
    song.artist = artist
    song.song= songtitle.split(".")[0]
    song.save()

def processSongs(album,artist):
    songs =os.listdir()
    for song in songs:
        print(" |-"+song)
        tagSong(song,album,artist)

def processAlbums(artist):
    albums = os.listdir()
    for album in albums:
        print("|-"+album)
        os.chdir(album)
        processSongs(album, artist)
        os.chdir("..")


def processArtists(entries):
    for artist in entries:
        print(artist)
        os.chdir(artist)
        processAlbums(artist)
        os.chdir("..")


def main():
    start = "testdata"
    os.chdir(start)
    entries = os.listdir()
    processArtists(entries)

main()