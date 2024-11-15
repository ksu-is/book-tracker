
# function to choose a category    

def category():
    category_input = input("Choose a category (Want to Read, Currently Reading, Read): ")
    if category_input == 'Want to Read':
        print("Want to Read: ")
    elif category_input == 'Currently Reading':
        print("Currently Reading: ")
    elif category_input == 'Read: ':
        print("Read: ")
    else:
        print
    

# function to print books title and author  
def book_title_author():
    book_title = input("Enter a book title: ")
    book_author = input("Enter the book's author: ")
    print("Book Title:",book_title, "by", book_author)
book_title_author()

