class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def addSong(self, song):
        self.songs.append(song)
        print(f"{song.title} added to '{self.name}'.")

    def show(self):
        print("\n")
        print(f"Playlist: {self.name}")
        for song in self.songs:
            print(f"- {song.showInfo()}")
