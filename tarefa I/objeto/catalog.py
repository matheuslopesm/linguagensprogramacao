from song import Song

class Catalog:
    def __init__(self):
        self.songs = []

    def addSong(self, song):
        self.songs.append(song)

    def listCatalog(self):
        print("============================================================")
        print("Song catalog:")
        for song in self.songs:
            print(f"- {song.showInfo()}")
        print("============================================================")
