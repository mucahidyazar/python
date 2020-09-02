from library import *

print("""
  Welcome to Library

  Processes
  1 Show Books
  2 Book Query
  3 Add Book
  4 Delete Book
  5 Increate Print Count

  Press Q to exit
""")

myLibrary = Library()

while True:
  process = input('What do yo want to do? #')
  if process == 'q':
    print('You are leaving from library...')
    print('Good bye...')
    break

  elif process == "1":
    myLibrary.showBooks()

  elif process == "2":
    name = input('Which book do you want to search? #')
    print('Searching the book')
    time.sleep(1)
    myLibrary.bookQuery(name)

  elif process == "3":
    name = input('Book name : #')
    author = input('Author : #')
    publisher = input('Publisher : #')
    bookType = input('bookType : #')
    printCount = int(input('printCount : #'))
    newBook = Book(name, author, publisher, bookType, printCount)
    print('Book is adding')
    time.sleep(1)
    myLibrary.addBook(newBook)
    print('Book was added')

  elif process == "4":
    name = input('Which book do you want to delete? #')
    cevap =input('Are you sure? # (Y/N)')
    if cevap == 'y':
      print('Book is deleting...')
      time.sleep(1)
      myLibrary.deleteBook(name)
      print('Book was deleted')

  elif process == "5":
    name = input('Which book do you want to get update its print count? #')
    print('Print count is increasing')
    time.sleep(1)
    myLibrary.increasePrint(name)
    print('Print count is increased')

  else:
    print('Wrong option')