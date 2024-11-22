
to_read = []
currently_reading = []
read = []
other = []
dates = []
completed_books = []

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
book = input("Enter book title and author: ")  
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
            elif chosen_category == 'q':
                if book == 'q':
                    break

# function to view books that have been tracked
def view_books():
     print("\nBooks In Your Library")
     print("Want to Read:",to_read)
     print("Currently Reading:",currently_reading)
     print("Read:",read)

# function to confirm date
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September','October','November','December']
day_in_month = [31,29,31,30,31,30,31,31,30,31,30,31]
def chosen_date(month, day):
     if month in months:
          months_index = month.index(month)
          amount_of_days = day_in_month[months_index]
          return 1 <= int(day) <= amount_of_days
     return False

# start date function
print("Enter start date: ")
while True:
     start_month = input("Month: ")
     start_day = input("Day: ")
     if chosen_date(start_month, start_day):
          break


# end date function
print("Enter end date: ")
while True:
     end_month = input("Month: ")
     end_day = input("Day: ")
     if chosen_date(end_month, end_day):
          break

# storing end dates and start dates
completed_books.append(start_month)
completed_books.append(start_day)
completed_books.append(end_month)
completed_books.append(end_day)

# calling the functions
category()
add_books()
view_books()
