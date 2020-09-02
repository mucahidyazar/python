from classes import *

print("""
  Welcome to Library

  Processes
  1 Add Song
  2 Delete Song
  3 Show All Songs
  4 Show an Album
  5 How Long That Album
  6 How Long All Songs

  Press Q to exit
""")

album = Album()


while True:
  process = input('What do you want to do?')
  if process == 'q':
    print('We are waiting for you again, see you now 🖐')
    break
  
  if process == '1':
    name = input('Song name: ')
    duration = int(input('Durability: '))
    albumName = input('Album name: ')
    singer = input('Singer: ')
    feat = input('Feat: ')
    production = input('Production: ')
    newSong = Song(name, duration, albumName, singer, feat, production)
    album.addSong(newSong)
  elif process == '2':
    songId = input('What is the song id that you want to delete? #')
    album.deleteSong(songId)
  elif process == '3':
    print('111111')
    album.showAllSongs()
  elif process == '4':
    albumName = input('What is the album name that you want to see? #')
    album.showAlbum(albumName)
  elif process == '5':
    albumName = input('What is the album name that you want to see? #')
    album.howLongThatAlbum(albumName)
  elif process == '6':
    album.howLongAllSongs()
  else:
    print('You chosed wrong choice, please try again')
