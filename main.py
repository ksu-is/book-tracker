
to_read = []
currently_reading = []
read = []

# function to choose a category
def category():
    while True:
        print("\nCategory:")
        print()
        print("1. Want to Read")
        print("2. Currently Reading")
        print("3. Read")
        print("4. View Library")
        print("5. View Stats")
        print("6. Quit")
        print("7. Remove a Book")
        decision = input("Choose a category(1-7): ").strip()
        if decision in ["1","2","3","5","6"]:
            return decision
        elif decision in ["4"]:
            view_books()
        elif decision in ["5"]:
            view_stats()
        elif decision in ["7"]:
            remove_book()
        else: 
            print("Invalid choice. Try again.")

#function to add a book to chosen category   
def add_books(chosen_category):
        while True:
            if chosen_category == "6":
                return False
            book = input("Enter book title and author: ").strip().title()
            if chosen_category == "1":
                to_read.append(book)
                print(book," added to 'Want to Read'")
                break
            elif chosen_category == "2":
                start = start_date()
                print(book + " added to 'Currently Reading', started on " + start)
                currently_reading.append((book,start))
                break      
            elif chosen_category == "3":
                start = start_date()
                end = end_date()
                read.append((book,start,end))
                print(book + " added to 'Read',read from", start + " - " + end)
                break

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
        end_month = input("End Month: ").strip().title()
        end_day = input("End Day: ").strip().title()
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

#function to remove book from category
def remove_book():
    print("\nRemove a Book")
    print("1. Want to Read")
    print("2. Currently Reading")
    print("3. Read")
    remove = input("Choose a category to remove from (1-3): ").strip()

    if remove == "1":
        book = input("Enter title and author to remove or 'q' to quit: ").strip().title()
        if book in to_read:
            to_read.remove(book)
            print(book, "was removed from 'Want to Read'.")
        else: 
            print(book, "was not found in 'Want to Read'. Try again")
    elif remove == "2":
        book = input("Enter title and author to remove: ").strip().title()
        if book in currently_reading:
            currently_reading.remove(book)
            print(book, "was removed from 'Currently Reading'.")
        else: 
            print(book, "was not found in 'Currently Reading'. Try again")
    elif remove == "3":
        book = input("Enter title and author to remove: ").strip().title()
        if book in read:
            read.remove(book)
            print(book, "was removed from 'Read'.")
        else: 
            print(book, "was not found in 'Read'. Try again")
    else:
        if book == 'q':
            view_books()

#function to view tracked dates for books
def tracked_dates():
     print("\nTracked Dates for Books:")
     for book in currently_reading:
        print(book[0]+': Started on',book[1])
     for book in read:
        print(book[0]+': Started on',book[1],',Finished on',book[2])

#function to view monthly stats
def view_stats():
    print("\nMonthly Reading Stats")
    month = input("Enter month to see stats: ").strip().title()
    count = 0
    for book in read:
        start_month = book[1].split()[0]
        if start_month.lower() == month.lower():
            count = count + 1
    print("You read",count,"book(s) in",month)


#function to call functions repeatedly
def call_functions():
    while True:
        decision = category()
        if decision == '7':
            remove_book()
        elif decision == '6':
            exit = input("Would you like to exit this program?: ").strip().lower()
            if exit == 'yes':
                print("Goodbye!")
                return False
            elif exit == 'no':
                add_books(decision)
            else:
                print("Invalid input.Try again.")
        elif decision == '5':
            view_stats()
        elif decision == '4':
            view_books()
        elif decision in ["1","2","3"]:
            add_books(decision)
        else:
            print("Invalid decision. Try again")

call_functions()