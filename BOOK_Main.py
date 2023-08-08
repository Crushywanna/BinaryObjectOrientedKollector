# Leaving room for the imports and any other comments
#Created for a Rutgers University MBS Final

import csv
# https://www.pythontutorial.net/python-basics/python-write-csv-file/
header = ['Title','Author','Reading Status','Book Format','Location']
#testdata = ["The Adventures of Huckleberry Finn","Mark Twain","Completed","Digital","Kindle"]


# Remember!  == for comparison , = for assigning
class book():
    _totalBook = [] # Got this from: https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python

    def __init__(self, Title, Author, datePublished=None, readingStatus=None, bookFormat=None, location=None):
        self.Title = Title
        self.Author = Author
        self.datePublished = datePublished
        self.readingStatus = readingStatus
        self.bookFormat = bookFormat
        self.location = location
        self._totalBook.append(self)
    
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
            return f"Title: {self.Title} \nAuthor: {self.Author} \nLocation: {self.location}\nBook Format: {self.bookFormat}\nReading Status: {self.readingStatus}\nDate Published: {self.datePublished}\n"

firstbook = book("The Adventures of Huckleberry Finn","Mark Twain")
firstbook.setAuthor = 'Mark Twain'
firstbook.setTitle = 'The Adventures of Huckleberry Finn'
secondbook = book("Pride and Prejudice","Jane Austen")
secondbook.setAuthor = 'Jane Austen'
secondbook.setTitle = 'Pride and Prejudice'

with open("Saved_BOOK.csv", 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

for i in book._totalBook:
    print(i)
#for i in firstbook:
    #writer.writerows(i)    