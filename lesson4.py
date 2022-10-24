def music_album(name_album,song,artist=None,group=None):
    album = {"name": name_album,
             "songs":song
    }
    if group:
        album["group"] = group
    if artist:
        album["artist"] = artist
    return album
count = 0
while count <= 3:
    name_album = input("Напиши название музыкального альбома:")
    name_artist = input("Напиши имя артиста:")
    name_group = None
    if not name_artist:
        name_group = input("Напиши название группы:")
    text = "Напиши название песни, но если они закончились напиши q:"
    album_songs = []
    while True:
        name_song = input(text)
        if name_song == "q":
            break
        album_songs.append(name_song)
        continue
    favorite_album = music_album(name_album,album_songs,name_artist,name_group)
    count +=1
    print(favorite_album)