
# function to choose a category    
def category():
    category_input = input("Choose a category (Want to Read, Currently Reading, Read): ")
    if category_input is 'Want to Read':
        print("Want to Read:",book_title_author)
    elif category_input is 'Currently Reading':
        print("Currently Reading:",book_title_author)
    elif category_input is 'Read':
        print("Read:",book_title_author)
    else:
        print("This category does not exist. Try again")


# function to print books title and author  
def book_title_author():
    book_title = input("Enter a book title: ")
    book_author = input("Enter the book's author: ")
    print("Book Title:",book_title, "by", book_author)
book_title_author()

