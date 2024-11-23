
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
        print("1.Want to Read")
        print("2.Currently Reading")
        print("3.Read")
        print("4.Other")
        return input("Choose a category (1-4): ")

#function to add a book to chosen category   
def add_books():
        while True:
            chosen_category = input("Enter your chosen category: ")
            book = input("Enter book title and author: ")

            if chosen_category == "1":
                to_read.append(book)
                print(book,"added to 'Want to Read")
            elif chosen_category == "2":
                currently_reading.append(book)
                print(book,"added to 'Currently Reading'")
                while True:
                    start_month = input("Start Month: ")
                    start_day = input("Start Day: ") 
                    if valid_date(start_month,start_day):
                        break
            elif chosen_category == "3":
                read.append(book)
                print(book,"added to 'Read'")
            elif chosen_category == "4":
                other.append(book)
                print(book,"added to 'Other'")
            elif chosen_category == 'q':
                if book == 'q':
                    break

#function to confirm date
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September','October','November','December']
day_in_month = [31,29,31,30,31,30,31,31,30,31,30,31]
def valid_date(months,day_in_month):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September','October','November','December']
    day_in_month = [31,29,31,30,31,30,31,31,30,31,30,31]

#start date function
def start_date():
    start_month = input("Month: ")
    start_day = input("Day: ")
    if start_month in months:
        months_index = start_month.index(start_month)
        amount_of_days = day_in_month[months_index]
        return 1 <= int(start_day) <= amount_of_days
    return False

#end date function
def end_date():
    end_month = input("Month: ")
    end_day = input("Day: ")
    if end_month in months:
        months_index = end_month.index(end_month)
        amount_of_days = day_in_month[months_index]
        return 1 <= int(end_day) <= amount_of_days
    return False
#print("Enter end date: ")
#while True:
     #end_month = input("Month: ")
     #end_day = input("Day: ")
     #if chosen_date(end_month, end_day):
          #break

#function to view books that have been tracked
#def view_books():
     #print("\nBooks In Your Library")
     #print("Want to Read:",to_read)
     #print("Currently Reading:",currently_reading)
     #print("Read:",read)

# storing end dates and start dates
#completed_books.append(start_month)
#completed_books.append(start_day)
#completed_books.append(end_month)
#completed_books.append(end_day)

# calling the functions
category()
add_books()
start_date()
end_date()
valid_date(months,day_in_month)
#view_books()





