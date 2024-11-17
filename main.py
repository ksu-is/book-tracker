to_read = []
currently_reading = []
read = []
other = []

# function to choose a category
def category():
    
    while True:
        print("\nCategory:")
        print()
        print("Want to Read")
        print("Currently Reading")
        print("Read")
        print("Other")
        return input("Choose a category: ")

# function to add a book to chosen category    
def add_books():
        chosen_category = input("Enter your chosen category: ")
        book = input("Enter book title: ")

        if chosen_category == "Want to Read":
            to_read.append(book)
            print(book,"added to 'Want to Read")
        elif chosen_category == "Currently Readinig":
            currently_reading.append(book)
            print(book,"added to 'Currently Reading'")
        elif chosen_category == "Read":
            read.append(book)
            print(book,"added to 'Read'")
        elif chosen_category == "Other":
            other.append(book)
            print(book,"added to 'Other'")
        else:
            print("Category does not exist. Try another.")

# function to view books that have been tracked
def view_books():
     print("\nBooks In Your Library")
     print(to_read)
     print(currently_reading)
     print(read)

category()
add_books()
view_books()
