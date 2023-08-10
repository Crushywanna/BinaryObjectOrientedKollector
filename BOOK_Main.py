# Leaving room for the imports and any other comments
#Created for a Rutgers University MBS Final
#https://github.com/Crushywanna/BinaryObjectOrientedKollector

# Shoutout to Sukhmeet Khalar (https://github.com/mithusingh32) for this idea. Way easier than randomly giving names to the books.
from faker import Faker# https://faker.readthedocs.io/en/master/
fake = Faker() # Kept forgetting to add this in. Without this being called, Faker doesn't work.
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

firstbook = book("The Adventures of Huckleberry Finn","Mark Twain")
firstbook.setAuthor = 'Mark Twain'
firstbook.setTitle = 'The Adventures of Huckleberry Finn'
secondbook = book("Pride and Prejudice","Jane Austen")
secondbook.setAuthor = 'Jane Austen'
secondbook.setTitle = 'Pride and Prejudice'

# Let's make some books using Faker!

for i in range(9998): # Only 9998 because I already made two books above, and I want to keep them.
    # Turns out "10KBooks" is not an approved variable? Can't start with an integer, so that was lame.
    TenKbook = book(Title=fake.catch_phrase(), # Holy COW. This got long. Kept each element to a single line for readability.
                    Author=fake.name(), # Creating an author
                    datePublished=fake.date(), # Creating a date
                    readingStatus=fake.random_element(elements=('Completed', 'In Progress', 'Not Started')), # Creating the reading status
                    bookFormat=fake.random_element(elements=('Digital', 'Physical')), # Creating the book format
                    location=fake.random_element(elements=('Home', 'Work', 'School', 'Other')) # Creating a location
                 )



# Open a CSV file for writing
with open("Saved_BOOK.csv", 'w', encoding='UTF8', newline='') as f:
    bookFields = ['Title', 'Author', 'Reading Status', 'Book Format', 'Location']
    writer = csv.DictWriter(f, fieldnames=bookFields)
    writer.writeheader()

    # Write data to the CSV file
    for i in book._totalBook:
        writer.writerow({ # The braces really threw me off. I was trying to use brackets, and it was not working. Documentation saved me though.
            'Title': i.Title,
            'Author': i.Author,
            'Reading Status': i.readingStatus,
            'Book Format': i.bookFormat,
            'Location': i.location
        })

# Print the book information
# While the above code saves the data to the preferred output (CSV) this print shows that information is being created.
# It can be commented out, since all it does is read the output from the TenKbook lists.
for i in book._totalBook:
    print(i)