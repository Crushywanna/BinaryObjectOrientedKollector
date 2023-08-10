# Actual program for the book library
# Called in BOOK_Main.py

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
            return (
                f"Title: {self.Title} \n"
                f"Author: {self.Author} \n"
                f"Location: {self.location}\n"
                f"Book Format: {self.bookFormat}\n"
                f"Reading Status: {self.readingStatus}\n"
                f"Date Published: {self.datePublished}\n")
    
    def __iter__(self):
        for i in self._totalBook:
            yield i
