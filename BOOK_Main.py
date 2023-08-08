# Leaving room for the imports and any other comments
#Created for a Rutgers University MBS Final

import csv


# Remember!  == for comparison , = for assigning
class book():

    def __init__(self, Title, Author, ISBNnum=None, datePublished=None, readingStatus=None, bookFormat=None, location=None):
        self.ISBNnum = ISBNnum
        self.Title = Title
        self.Author = Author
        self.datePublished = datePublished
        self.readingStatus = readingStatus
        self.bookFormat = bookFormat
        self.location = location

    def getISBN(self): # Getting the ISBN // OPTIONAL FOR USER
        return self.ISBNnum
    
    def setISBN(self, ISBNnum): # Setting the ISBN // OPTIONAL FOR USER
        self.ISBNnum = ISBNnum
    
    def getTitle(self): # Getting Title
        return self.Title
    
    def setTitle(self, Title): # Setting Title
        self.Title = Title
    
    def getAuthor(self):  # Getting Author
        return self.Title
    
    def setAuthor(self, Author): # Setting Author
        self.Author = Author

    def getdatePublished(self): # Getting Publication date // OPTIONAL FOR USER
        return self.datePublished
    
    def setdatePublished(self, datePublished): # Setting publication date // OPTIONAL FOR USER
        self.datePublished = datePublished
    
    def getreadingStatus(self): # Getting Reading Status // OPTIONAL FOR USER
        return self.readingStatus
    
    def setreadingStatus(self, readingStatus): # Setting Reading Status // OPTIONAL FOR USER
        self.readingStatus = readingStatus

    def getbookFormat(self): # Getting book format // OPTIONAL FOR USER
        return self.bookFormat
    
    def setbookFormat(self, bookFormat): # Setting book format // OPTIONAL FOR USER
        self.bookFormat = bookFormat

    def getlocation(self): # Getting location // OPTIONAL FOR USER
        return self.location
    
    def setlocation(self, location): # Setting location // OPTIONAL FOR USER
        self.location = location

    def __str__(self): # self printer
            return f"Title: {self.Title} \nAuthor: {self.Author} \nISBN: {self.ISBNnum} \nLocation: {self.location}\nBook Format: {self.bookFormat}\nReading Status: {self.readingStatus}\nDate Published: {self.datePublished}\n"

firstbook = book("The Adventures of Huckleberry Finn","Mark Twain")
firstbook.setAuthor = 'Mark Twain'
firstbook.setTitle = 'The Adventures of Huckleberry Finn'

print(firstbook)