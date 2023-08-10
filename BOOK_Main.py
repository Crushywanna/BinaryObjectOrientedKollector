# Leaving room for the imports and any other comments
#Created for a Rutgers University MBS Final
#https://github.com/Crushywanna/BinaryObjectOrientedKollector

# Shoutout to my friend Sukhmeet Khalar for this idea. He listened to me complain and showed me this instead. Way easier than randomly giving names to the books.
from faker import Faker# https://faker.readthedocs.io/en/master/
fake = Faker() # Kept forgetting to add this in. Without this being called, Faker doesn't work.
import csv
from BOOK_lib import *
# https://www.pythontutorial.net/python-basics/python-write-csv-file/
header = ['Title','Author','Reading Status','Book Format','Location']


# I make all of the books first, since this is a demo of the software. I can't necessarily demo with no information.

firstbook = book("The Adventures of Huckleberry Finn","Mark Twain")
firstbook.setAuthor = 'Mark Twain'
firstbook.setTitle = 'The Adventures of Huckleberry Finn'
secondbook = book("Pride and Prejudice","Jane Austen")
secondbook.setAuthor = 'Jane Austen'
secondbook.setTitle = 'Pride and Prejudice'

# Let's make some books using Faker!

# I decided to only make 20 books for the demo, to make the user selection easier. This is easily scaled to over 1M books but readability won't be great.
for i in range(18): # Only 18 because I already made two books above, and I want to keep them.
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
    bookFields = ['Title', 'Author', 'datePublished','Reading Status', 'Book Format', 'Location']
    writer = csv.DictWriter(f, fieldnames=bookFields)
    writer.writeheader()

    # Write data to the CSV file
    for i in book._totalBook:
        writer.writerow({ # The braces really threw me off. I was trying to use brackets, and it was not working. Documentation saved me though.
            'Title': i.Title,
            'Author': i.Author,
            'datePublished': i.datePublished,
            'Reading Status': i.readingStatus,
            'Book Format': i.bookFormat,
            'Location': i.location
        })

# Print the book information
# While the above code saves the data to the preferred output (CSV) this print shows that information is being created.
# It can be commented out, since all it does is read the output from the TenKbook lists.
# for i in book._totalBook:
#     print(i)

# I "stole" this from my undergrad assignment in Python. I genuinely don't recall much of the class but this was saved in my notes.
# It was more a FAQ using a key pair? But I can just make it user input.
Runner = True
while Runner:
    print ("""
====================================
    BOOK Program
====================================
    0: Exit / Quit
    1: List Books
    2: Enter a new book
    3: Delete the last book
    """) # Triple Quotes to allow for multi-line prints
         
    Choice=input ("What would you like to do? ") 
    if Choice=="0":
            print ("\n Goodbye")
            break #Allows the program to escape the loop
        
    elif Choice=="1":
        print ("""
====================================
   List of Books
====================================""")
        for i in book._totalBook:
            print(i)

    elif Choice=="2":
        print("""
====================================
   Creating a new book
====================================""")
        print ("Insert the new book's Title on the next line: ")
        newTitle = input() # New Title
        print ("Insert the new book's Author on the next line: ")
        newAuthor = input() # New Author
        newbook = book(Title=newTitle, Author=newAuthor) # Creating the new book
        print ("Do you want to insert a reading status? (Y/N)")
        if input() == "Y": # I'm not sure how to error check this without the code getting silly. TODO?
            print ("Insert the new book's reading status on the next line: ")
            newReadingStatus = input()
            newbook.setreadingStatus = newReadingStatus
        else:
            pass
        print ("Do you want to insert a Publishing Date? (Y/N)")
        if input() == "Y":
            print ("Insert the new book's publishing date on the next line in MM/DD/YYYY format: ") # I have no clue at this time how to error check this without the code getting silly. TODO?
            newdatePublished = input()
            newbook.setdatePublished = newdatePublished
        else:
            pass
        print ("Do you want to insert a Book Format? (Y/N)")
        if input() == "Y": # I'm not sure how to error check this without the code getting silly. TODO?
            print ("Insert the new book's format on the next line using either Digital or Physical: ")
            if input() == "Digital" or "digital":
                newbookFormat = "Digital"
            elif input() == "Physical" or "physical":
                newbookFormat = "Physical"
            else:
                print ("Format must be either Digital or Physical. Please try again.")
                pass
            newbookFormat = input()
            newbook.setbookFormat = newbookFormat
        else:
            pass
        print ("Do you want to insert a Location? (Y/N)")
        if input() == "Y":# I'm not sure how to error check this without the code getting silly. TODO?
            print ("Insert the new book's location on the next line: ")
            newlocation = input()
            newbook.setlocation = newlocation
        else:
            pass
    
    elif Choice=="3":
        print("""
====================================
   Deleting the last book
====================================""")
        if len(book._totalBook) > 0: # This checks that there really is books to delete
            lastbook = book._totalBook[-1]
            book._totalBook.pop() # This was the only way I could figure out how to implement a data structure so late into the program. I had already thought of how I was going to begin the program before Unit 6 was started. :/
            print ("The last book was deleted.")
        else:
            print ("There are no books to delete.")
            print ("Please add a book before trying to delete one.")

#The lines below are the error management lines
#They prevent miskeys during the menu selection      
    elif   Choice !="":
        print ("\n Invalid Choice. Please try again or press 0 to exit: ")
    elif Choice == "":
        print ("you will now exit")
print (" Program Finished")
