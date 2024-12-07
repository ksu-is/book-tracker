
to_read = []
currently_reading = []
read = []

# function to choose a category
def category():
    while True:
        print("\nCategory:")
        print()
        print("1.Want to Read")
        print("2.Currently Reading")
        print("3.Read")
        print("4.View Library")
        print("5.Quit")
        decision = input("Choose a category(1-5): ")
        if decision in ["1","2","3","5"]:
            return decision
        elif decision in ["4"]:
            print(view_books)
        else: 
            print("Invalid choice. Try again.")

#function to add a book to chosen category   
def add_books():
        while True:
            chosen_category = input("Enter your chosen category: ")
            if chosen_category == "5":
                return False
            book = input("Enter book title and author: ")
            if chosen_category == "1":
                to_read.append(book)
                print(book," added to 'Want to Read")
                break
            elif chosen_category == "2":
                start = start_date()
                print(book + " added to 'Currently Reading', started on " + start)
                currently_reading.append((book,start))
                    
            elif chosen_category == "3":
                start = start_date()
                end = end_date()
                read.append((book,start,end))
                print(book + " added to 'Read',read from", start + "to" + end)
                break
            elif chosen_category == "4":
                print(view_books)

#function to confirm date
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September','October','November','December']
day_in_month = [31,29,31,30,31,30,31,31,30,31,30,31]
def valid_date(month,day):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September','October','November','December']
    day_in_month = [31,29,31,30,31,30,31,31,30,31,30,31]
    if month in months:
        month_index = months.index(month)
        return 1 <= int(day) <= day_in_month[month_index]

#start date function
def start_date():
    while True:
        start_month = input("Start Month: ")
        start_day = input("Start Day: ")
        if valid_date(start_month, start_day):
            return start_month  + " " + start_day
        else:
            print("Invalid date. Try again.")

#end date function
def end_date():
    while True:
        end_month = input("End Month: ")
        end_day = input("End Day: ")
        if valid_date(end_month, end_day):
            return (end_month  + " " + end_day)
        else:
            print("Invalid date. Try again.")

#function to view books that have been tracked
def view_books():
     print("\nBooks In Your Library")
     print("Want to Read:",to_read)
     print("Currently Reading:",[book[0] for book in currently_reading])
     print("Read:",[book[0] for book in read])
     print("\nTracked Dates for Books:")
     for book in currently_reading:
        print(book[0]+': Started on',book[1])
     for book in read:
        print(book[0]+': Started on',book[1],',Finished on',book[2])

#function to call functions repeatedly
def call_functions():
    while True:
        category()
        add_books()
        view_books()

call_functions()






