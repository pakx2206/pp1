class music():
    def __init__(self, performer, song, album, year) -> None:
        self.performer = performer
        self.song = song
        self.album = album
        self.year = year

    def __str__(self) -> str:
        return (f'Performer:{self.performer}\nSong:{self.song}\nAlbum:{self.album}\nYear:{self.year}')


x = music("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", "2017")
print(x)
