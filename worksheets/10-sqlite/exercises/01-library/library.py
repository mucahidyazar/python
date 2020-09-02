import sqlite3
import time

class Book():

  def __init__(self, name, author, publisher, bookType, printCount):
    self.name = name
    self.author = author
    self.publisher = publisher
    self.bookType = bookType
    self.printCount = printCount

  def __str__(self):
    return """
      Book name: {}
      Author: {}
      Publisher: {}
      Type: {}
      Print count: {}
    """.format(self.name, self.author, self.publisher, self.bookType, self.printCount)

  







class Library():

  def __init__(self):
    self.makeConnect()

  def makeConnect(self):
    self.connect = sqlite3.connect('library.db')
    self.cursor = self.connect.cursor()
    
    query = 'CREATE TABLE IF NOT EXISTS books (name TEXT, author TEXT, publisher TEXT, self TEXT, printCount INT)'
    self.cursor.execute(query)
    self.connect.commit()
  
  def diconnect(self):
    self.connect.close()

  def showBooks(self):
    query = "SELECT * FROM books"
    self.cursor.execute(query)
    books = self.cursor.fetchall()
    if len(books) == 0:
      print('Kutuphanede kitap bulunmuyor...')
    else:
      for i in books:
        book = Book(i[0], i[1], i[2], i[3], i[4])
        print(book)

  def bookQuery(self, name):
    query = 'SELECT * FROM books where name = ?'
    self.cursor.execute(query, (name, ))
    books = self.cursor.fetchall()
    if len(books) == 0:
      print('There is no book')
    else:
      book = Book(books[0][0], books[0][1], books[0][2], books[0][3], books[0][4])
      print(book)

  def addBook(self, book):
    query = 'INSERT INTO books VALUES(?,?,?,?,?)'
    self.cursor.execute(query, (book.name, book.author, book.publisher, book.bookType, book.printCount))
    self.connect.commit()

  def deleteBook(self, name):
    query = 'DELETE FROM books WHERE name = ?'
    self.cursor.execute(query, (name, ))
    self.connect.commit()

  def increasePrint(self, name):
    query = 'SELECT * FROM books WHERE name = ?'
    self.cursor.execute(query, (name, ))
    books = self.cursor.fetchall()

    if len(books) == 0:
      print('There is no book')
    else:
      printCount = books[0][4]
      printCount += 1

      query2 = 'UPDATE books SET printCount = ? WHERE name = ?'
      self.cursor.execute(query2, (printCount, name))
      self.connect.commit()