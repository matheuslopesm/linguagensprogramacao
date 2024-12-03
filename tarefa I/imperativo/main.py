from catalog import catalog

playlists = {}

def playSong(song):
    print("\n")
    print(f" ♪ Playing: {song['title']} of {song['author']} ({song['time']})...")

def addToPlaylist(playlistName, song):
    if playlistName not in playlists:
        playlists[playlistName] = []
    playlists[playlistName].append(song)
    print(f"'{song['title']}' added to playlist: '{playlistName}'.")

def showPlaylist(playlistName):
    if playlistName in playlists:
        print('\n')
        print(f"Playlist: {playlistName}")
        for song in playlists[playlistName]:
            print(f"- {song['title']} of {song['author']}")
    else:
        print(f"The playlist '{playlistName}' dont exists, yet!")
        print("\n")

def listCatalog():
    print("============================================================")
    print("Song catalog:")
    for song in catalog:
        print(f"- {song['title']} of {song['author']} ({song['time']})")
    print("============================================================")

listCatalog()
showPlaylist("My favorite")
addToPlaylist("My favorite", catalog[0])
addToPlaylist("My favorite", catalog[1])
showPlaylist("My favorite")
playSong(catalog[0])
