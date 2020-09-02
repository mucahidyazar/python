import sqlite3
import uuid
import time

class Song():

  def __init__(self, name, duration, album, singer, feat, production):
    self.id = uuid.uuid4()
    self.name = name
    self.duration = duration
    self.album = album
    self.singer = singer
    self.feat = feat
    self.production = production

  def __str__(self):
    return {
      'id': self.id,
      'name': self.name,
      'duration': self.duration,
      'album': self.album,
      'singer': self.singer,
      'feat': self.feat,
      'production': self.production
    }

class Album():

  def __init__(self):
    self.connectDatabase()

  def __str__(self):
    print("""
      Singer Name: Mike Anderson
        Album Name: Sun
          1 Sunny days
          2 Rainny days
          3 Love
          4 Like the ways
          5 My name
    """)

  def __len__(self):
    songs = self.cursor.execute('SELECT * from songs')
    return len(songs)

  def connectDatabase(self):
    self.connectDatabase = sqlite3.connect('songs.db')
    self.cursor = self.connectDatabase.cursor()
    self.cursor.execute('CREATE TABLE IF NOT EXISTS songs (id TEXT, name TEXT, duration INT, album TEXT, singer TEXT, feat TEXT, production TEXT)')
    self.connectDatabase.commit()

  def disconnectDatabase(self):
    self.connectDatabase.close()

  def addSong(self, song):
    print('Adding...')
    self.cursor.execute('INSERT INTO songs VALUES(?,?,?,?,?,?,?)', (str(song.id), song.name, song.duration, song.album, song.singer, song.feat, song.production))
    self.connectDatabase.commit()
    time.sleep(.3)
    print('Added')

  def deleteSong(self, id):
    print('Deleting...')
    self.cursor.execute('DELETE FROM songs WHERE id = ?', (id,))
    self.connectDatabase.commit()
    print('Deleted.')

  def showAllSongs(self):
    self.cursor.execute('SELECT * FROM songs')
    songs = self.cursor.fetchall()
    for song in songs:
      print('--->',  song)

  def showAlbum(self, album):
    self.cursor.execute('SELECT * FROM songs WHERE album = ?', (album,))
    album = self.cursor.fetchall()
    print('Album :',album)
    for song in album:
      print('--->',song[0], song)

  def howLongThatAlbum(self, album):
    self.cursor.execute('SELECT * FROM songs WHERE album = ?', (album,))
    album = self.cursor.fetchall()
    total = 0
    for song in album:
      total+=song[2]
    print('{} duration is {} seconds'.format(album, total))
  def howLongAllSongs(self):
    self.cursor.execute('SELECT * FROM songs')
    songs = self.cursor.fetchall()
    total = 0
    for song in songs:
      total+=song[2]
    print('All songs durabilities are {} seconds'.format(total))

  