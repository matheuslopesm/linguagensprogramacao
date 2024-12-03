from catalog import Catalog
from playlist import Playlist
from song import Song

catalog = Catalog()
catalog.addSong(Song("Waiting for the End", "Linkin Park", "3:52"))
catalog.addSong(Song("Head Full of Dreams", "Coldplay", "3:44"))

catalog.listCatalog()

playlist = Playlist("My favorite")
playlist.addSong(catalog.songs[0])
playlist.addSong(catalog.songs[1])
playlist.show()
