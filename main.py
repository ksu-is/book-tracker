
to_read = []
currently_reading = []
read = []
other = []
dates = []
monthly_stats = []

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
        while True:
            chosen_category = input("Enter your chosen category: ")
            book = input("Enter book title and author: ")

            if chosen_category == "Want to Read":
                to_read.append(book)
                print(book,"added to 'Want to Read")
            elif chosen_category == "Currently Reading":
                currently_reading.append(book)
                print(book,"added to 'Currently Reading'")
                start_date = input("Enter start date: ")
            elif chosen_category == "Read":
                read.append(book)
                print(book,"added to 'Read'")
                start_date = input("Enter start date: ")
                end_date = input("Enter end date: ")
                dates.append(start_date)
                dates.append(end_date)
            elif chosen_category == "Other":
                other.append(book)
                print(book,"added to 'Other'")
            else:
                if chosen_category and book == 'q':
                     break

# function to view books that have been tracked
def view_books():
     print("\nBooks In Your Library")
     print("Want to Read:",to_read)
     print("Currently Reading:",currently_reading)
     print("Read:",read)

def monthly_stats():
     print("\nMonthly Stats")
     print()
     date = input("What is today's date?: ")
     if date in range[1/1:1/31]:
          monthly_stats.append(date)
     
     

# calling the functions
category()
add_books()
view_books()
monthly_stats()

     